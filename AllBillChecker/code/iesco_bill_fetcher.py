#!/usr/bin/env python3
"""
IESCO Duplicate Bill Fetcher
Fetches electricity bill details from Islamabad Electric Supply Company (IESCO) 
using a 10-digit Consumer ID (Customer ID) or a 14-digit Reference Number.
"""

import sys
import argparse
import json
import re
from typing import Dict, Any, Optional
import requests
from bs4 import BeautifulSoup

# Base PITC URL for IESCO duplicate bills
IESCO_BILL_URL = "https://bill.pitc.com.pk/iescobill"

def clean_text(text: Optional[str]) -> str:
    """Helper to clean up whitespaces and special characters in scraped text."""
    if not text:
        return ""
    # Replace non-breaking spaces and hidden control chars
    text = text.replace('\xa0', ' ').replace('\u200e', '').replace('\u200f', '')
    return " ".join(text.split()).strip()

def parse_bill_details(soup: BeautifulSoup, identifier: str) -> Dict[str, Any]:
    """
    Parses the bill HTML returned by the PITC portal.
    Extracts key billing fields dynamically using regex matching on cell contents.
    """
    # Grab all text elements to scan for labels
    cells = []
    for tag in soup.find_all(['td', 'th', 'span', 'div']):
        text = clean_text(tag.get_text())
        if text:
            cells.append((tag, text))

    # Initialize resulting data dictionary
    data = {
        "queried_id": identifier,
        "consumer_id": "",
        "reference_no": "",
        "consumer_name": "",
        "consumer_address": "",
        "billing_month": "",
        "due_date": "",
        "payable_within_due_date": "",
        "late_payment_surcharge": "",
        "payable_after_due_date": "",
        "units_consumed": "",
        "meter_no": "",
        "connection_date": "",
        "tariff": "",
        "load": ""
    }

    # Helper function to find adjacent cell value in tables
    def get_sibling_val(label_regex: str) -> str:
        for tag, text in cells:
            if re.search(label_regex, text, re.IGNORECASE):
                # Try finding the next sibling element in the DOM
                sibling = tag.find_next_sibling(['td', 'th', 'span'])
                if sibling:
                    val = clean_text(sibling.get_text())
                    if val:
                        return val
                # Alternately, search siblings inside the same row
                parent = tag.parent
                if parent:
                    row_cells = parent.find_all(['td', 'th'])
                    try:
                        idx = row_cells.index(tag)
                        if idx + 1 < len(row_cells):
                            val = clean_text(row_cells[idx + 1].get_text())
                            if val:
                                return val
                    except ValueError:
                        pass
        return ""

    # Extract fields using targeted regex patterns
    data["billing_month"] = get_sibling_val(r"billing\s*month")
    data["due_date"] = get_sibling_val(r"due\s*date")
    data["payable_within_due_date"] = get_sibling_val(r"payable\s*within\s*due\s*date|amount\s*payable\s*within|payable\s*by\s*due\s*date")
    data["late_payment_surcharge"] = get_sibling_val(r"late\s*payment\s*surcharge|surcharge|l\.p\.s")
    data["payable_after_due_date"] = get_sibling_val(r"payable\s*after\s*due\s*date|amount\s*payable\s*after|payable\s*after")
    data["units_consumed"] = get_sibling_val(r"units\s*consumed|total\s*units|units")
    data["reference_no"] = get_sibling_val(r"reference\s*no|ref\s*no")
    data["consumer_id"] = get_sibling_val(r"customer\s*id|consumer\s*id")
    data["consumer_name"] = get_sibling_val(r"name\s*&\s*address|consumer\s*name|name")
    data["consumer_address"] = get_sibling_val(r"address")
    data["meter_no"] = get_sibling_val(r"meter\s*no|mtr\s*no")
    data["connection_date"] = get_sibling_val(r"connection\s*date")
    data["tariff"] = get_sibling_val(r"tariff")
    data["load"] = get_sibling_val(r"sanctioned\s*load|load")

    # Fallback to direct regex searches over the entire body text if fields are empty
    full_text = clean_text(soup.get_text())
    
    if not data["reference_no"]:
        ref_match = re.search(r'\b\d{14}[a-zA-Z]?\b', full_text)
        if ref_match:
            data["reference_no"] = ref_match.group(0)
            
    if not data["consumer_id"]:
        cust_match = re.search(r'\b\d{10}\b', full_text)
        if cust_match:
            data["consumer_id"] = cust_match.group(0)

    # Clean numeric fields (remove commas, extract only digit sequences)
    for key in ["payable_within_due_date", "late_payment_surcharge", "payable_after_due_date", "units_consumed"]:
        val = data[key]
        if val:
            num_match = re.search(r'[\d,]+(?:\.\d+)?', val)
            if num_match:
                data[key] = num_match.group(0).replace(",", "")
            else:
                data[key] = ""

    return data

def fetch_iesco_bill(identifier: str) -> Dict[str, Any]:
    """
    Fetches the duplicate bill details using either:
    - 10-digit Customer ID / Consumer ID
    - 14-digit Reference Number (digits only, e.g. 01123456789012)
    
    Returns:
        Dict[str, Any] containing parsed bill fields.
    """
    # Remove all non-digits from input
    cleaned_id = re.sub(r'\D', '', identifier)
    
    if len(cleaned_id) == 10:
        is_ref_no = False
    elif len(cleaned_id) == 14:
        is_ref_no = True
    else:
        raise ValueError("Invalid identifier format. Please provide a 10-digit Consumer ID or a 14-digit Reference Number.")
        
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": IESCO_BILL_URL
    }
    
    # Step 1: GET page to initialize the ASP.NET ViewState and tokens
    try:
        r = session.get(IESCO_BILL_URL, headers=headers, timeout=15)
        r.raise_for_status()
    except requests.RequestException as e:
        raise ConnectionError(f"Failed to connect to IESCO billing portal: {e}")
        
    soup = BeautifulSoup(r.text, 'html.parser')
    
    try:
        viewstate = soup.find('input', {'name': '__VIEWSTATE'}).get('value')
        viewstate_gen = soup.find('input', {'name': '__VIEWSTATEGENERATOR'}).get('value')
        event_validation = soup.find('input', {'name': '__EVENTVALIDATION'}).get('value')
        req_token = soup.find('input', {'name': '__RequestVerificationToken'}).get('value')
    except (AttributeError, TypeError) as e:
        raise ValueError(f"Could not parse authentication/state tokens from PITC portal. The page structure might have changed: {e}")

    # Step 2: If we are using a Consumer ID, execute an ASP.NET postback to switch fields
    if not is_ref_no:
        payload_postback = {
            "__EVENTTARGET": "rbSearchByList$1",
            "__EVENTARGUMENT": "",
            "__LASTFOCUS": "",
            "__VIEWSTATE": viewstate,
            "__VIEWSTATEGENERATOR": viewstate_gen,
            "__EVENTVALIDATION": event_validation,
            "__RequestVerificationToken": req_token,
            "rbSearchByList": "appno",
            "searchTextBox": "",
            "ruCodeTextBox": ""
        }
        
        try:
            r = session.post(IESCO_BILL_URL, headers=headers, data=payload_postback, timeout=15)
            r.raise_for_status()
        except requests.RequestException as e:
            raise ConnectionError(f"Failed during IESCO search initialization: {e}")
            
        soup = BeautifulSoup(r.text, 'html.parser')
        
        try:
            viewstate = soup.find('input', {'name': '__VIEWSTATE'}).get('value')
            viewstate_gen = soup.find('input', {'name': '__VIEWSTATEGENERATOR'}).get('value')
            event_validation = soup.find('input', {'name': '__EVENTVALIDATION'}).get('value')
            req_token = soup.find('input', {'name': '__RequestVerificationToken'}).get('value')
        except (AttributeError, TypeError) as e:
            raise ValueError(f"Failed to refresh state tokens after selecting Consumer ID mode: {e}")

    # Step 3: Send POST to perform the actual query
    payload_search = {
        "__EVENTTARGET": "",
        "__EVENTARGUMENT": "",
        "__LASTFOCUS": "",
        "__VIEWSTATE": viewstate,
        "__VIEWSTATEGENERATOR": viewstate_gen,
        "__EVENTVALIDATION": event_validation,
        "__RequestVerificationToken": req_token,
        "rbSearchByList": "appno" if not is_ref_no else "refno",
        "searchTextBox": cleaned_id,
        "ruCodeTextBox": "",
        "btnSearch": "Search"
    }
    
    try:
        r = session.post(IESCO_BILL_URL, headers=headers, data=payload_search, timeout=20)
        r.raise_for_status()
    except requests.RequestException as e:
        raise ConnectionError(f"Failed to query the IESCO bill: {e}")
        
    # Check if the PITC portal redirected back to index instead of displaying the duplicate bill
    if "iescobill/general" not in r.url and "general?" not in r.url:
        soup = BeautifulSoup(r.text, 'html.parser')
        error_msg = soup.find('span', {'id': 'lblinvalidmsg'})
        if error_msg:
            raise ValueError(f"IESCO search error: {clean_text(error_msg.get_text())}")
        raise ValueError("Bill details page was not returned. The provided ID may be invalid or not in the system.")
        
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # Check if the page has a "bill-not-found" block
    if soup.find(class_="bill-not-found"):
        raise ValueError("Bill not found. The provided ID may be invalid or does not have an active bill.")
        
    # Step 4: Parse bill details and return
    return parse_bill_details(soup, cleaned_id)

def main():
    parser = argparse.ArgumentParser(
        description="Connects to IESCO and fetches details of the duplicate bill using Consumer ID or Reference Number.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python iesco_bill_fetcher.py --id 1234567890
  python iesco_bill_fetcher.py --id 01123456789012 --json
"""
    )
    parser.add_argument(
        "-i", "--id",
        required=True,
        help="The 10-digit Consumer/Customer ID or 14-digit Reference Number."
    )
    parser.add_argument(
        "-j", "--json",
        action="store_true",
        help="Output the bill details in raw JSON format (useful for piping/scripting)."
    )

    args = parser.parse_args()

    try:
        bill_data = fetch_iesco_bill(args.id)
        
        if args.json:
            print(json.dumps(bill_data, indent=2))
        else:
            print("\n" + "="*50)
            print("         IESCO BILL DETAILS SUMMARY")
            print("="*50)
            print(f"Queried ID:             {bill_data['queried_id']}")
            print(f"Consumer ID (Cust ID):  {bill_data['consumer_id'] or 'N/A'}")
            print(f"Reference Number:       {bill_data['reference_no'] or 'N/A'}")
            print(f"Billing Month:          {bill_data['billing_month'] or 'N/A'}")
            print(f"Consumer Name:          {bill_data['consumer_name'] or 'N/A'}")
            print(f"Consumer Address:       {bill_data['consumer_address'] or 'N/A'}")
            print(f"Tariff / Sanc. Load:    {bill_data['tariff'] or 'N/A'} / {bill_data['load'] or 'N/A'}")
            print(f"Units Consumed:         {bill_data['units_consumed'] or 'N/A'} kWh")
            print("-"*50)
            print(f"Payable Within Due Date:{bill_data['payable_within_due_date'] or 'N/A'} PKR")
            print(f"Due Date:               {bill_data['due_date'] or 'N/A'}")
            print(f"Late Surcharge:         {bill_data['late_payment_surcharge'] or 'N/A'} PKR")
            print(f"Payable After Due Date: {bill_data['payable_after_due_date'] or 'N/A'} PKR")
            print("="*50 + "\n")
            
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
