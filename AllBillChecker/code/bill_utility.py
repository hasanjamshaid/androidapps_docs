#!/usr/bin/env python3
"""
Common utilities and helpers for PITC-based electricity bill scrapers.
Supports IESCO, LESCO, MEPCO, FESCO, PESCO, GEPCO, QESCO, and HESCO portals.
"""

import re
from typing import Dict, Any, Optional
import requests
from bs4 import BeautifulSoup

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
    Extracts key billing fields dynamically using cleaned label matching.
    """
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

    # Helper function to remove Urdu characters and normalize whitespace
    def clean_lbl(text: str) -> str:
        if not text:
            return ""
        # Remove non-ASCII characters (like Urdu translations)
        text = re.sub(r'[^\x00-\x7F]+', '', text)
        return " ".join(text.split()).strip().upper()

    # Find value by matching English labels
    def get_val_by_label(label_regex: str) -> str:
        # Search in label elements first
        for div in soup.find_all(class_=re.compile(r'label-row|label|right-panel-label-row', re.IGNORECASE)):
            lbl_text = clean_lbl(div.get_text())
            if re.search(label_regex, lbl_text, re.IGNORECASE):
                # Try sibling element first
                sibling = div.find_next_sibling()
                if sibling:
                    val = clean_text(sibling.get_text())
                    if val:
                        return val
                # Try sibling within parent
                parent = div.parent
                if parent:
                    val_el = parent.find(class_=re.compile(r'val|amount|date', re.IGNORECASE))
                    if val_el and val_el != div:
                        val = clean_text(val_el.get_text())
                        if val:
                            return val

        # Fallback: search all span, div, td, th elements
        for tag in soup.find_all(['span', 'div', 'td', 'th']):
            lbl_text = clean_lbl(tag.get_text())
            if re.search(label_regex, lbl_text, re.IGNORECASE):
                sibling = tag.find_next_sibling()
                if sibling:
                    val = clean_text(sibling.get_text())
                    if val:
                        return val
        return ""

    # Populate basic fields
    data["reference_no"] = get_val_by_label(r"^reference\s*no|ref\s*no")
    data["consumer_id"] = get_val_by_label(r"^consumer\s*id|cust\s*id|customer\s*id")
    data["billing_month"] = get_val_by_label(r"^bill\s*month|billing\s*month")
    data["due_date"] = get_val_by_label(r"due\s*date")
    data["units_consumed"] = get_val_by_label(r"^units$|units\s*consumed")
    data["meter_no"] = get_val_by_label(r"^meter\s*no|mtr\s*no")
    data["tariff"] = get_val_by_label(r"^tariff$|tariff\s*category")
    data["load"] = get_val_by_label(r"^san\s*load|^sanctioned\s*load|^load$")

    # Extract payment fields (using direct CSS classes first if available)
    payable_within_el = soup.find(class_='payable-card-amount')
    if payable_within_el:
        data["payable_within_due_date"] = clean_text(payable_within_el.get_text())
    else:
        data["payable_within_due_date"] = get_val_by_label(r"payable\s*within\s*due\s*date|amount\s*payable\s*within|payable\s*by\s*due\s*date")

    late_surcharge_el = soup.find(class_='lp-surcharge-top-val')
    if late_surcharge_el:
        data["late_payment_surcharge"] = clean_text(late_surcharge_el.get_text())
    else:
        data["late_payment_surcharge"] = get_val_by_label(r"late\s*payment\s*surcharge|surcharge|l\.p\s*surcharge|l\.p\.s")

    payable_after_el = soup.find(class_='lp-surcharge-bottom-val')
    if payable_after_el:
        data["payable_after_due_date"] = clean_text(payable_after_el.get_text())
    else:
        data["payable_after_due_date"] = get_val_by_label(r"payable\s*after\s*due\s*date|amount\s*payable\s*after|payable\s*after")

    # Parse connection date and other details from any textarea elements (QR code text)
    for textarea in soup.find_all('textarea'):
        raw_txt = textarea.get_text()
        if "CONN DATE:" in raw_txt:
            conn_match = re.search(r'CONN\s*DATE:\s*([^\r\n]+)', raw_txt, re.IGNORECASE)
            if conn_match:
                data["connection_date"] = clean_text(conn_match.group(1))
            # Also use textarea as fallback for other fields if they are missing
            if not data["reference_no"]:
                ref_match = re.search(r'REF\s*NO:\s*([^\r\n]+)', raw_txt, re.IGNORECASE)
                if ref_match:
                    data["reference_no"] = clean_text(ref_match.group(1))
            if not data["consumer_id"]:
                cid_match = re.search(r'CONSUMER\s*ID:\s*([^\r\n]+)', raw_txt, re.IGNORECASE)
                if cid_match:
                    data["consumer_id"] = clean_text(cid_match.group(1))
            if not data["units_consumed"]:
                units_match = re.search(r'UNITS:\s*([^\r\n]+)', raw_txt, re.IGNORECASE)
                if units_match:
                    data["units_consumed"] = clean_text(units_match.group(1))
            if not data["load"]:
                load_match = re.search(r'SAN\s*LOAD:\s*([^\r\n]+)', raw_txt, re.IGNORECASE)
                if load_match:
                    data["load"] = clean_text(load_match.group(1))

    # Parse Name and Address
    name_address = get_val_by_label(r"^name\s*&\s*address")
    if name_address:
        # Separate Name and Address
        parts = [p.strip() for p in name_address.split(',')]
        if len(parts) > 1:
            if any(parts[1].upper().startswith(prefix) for prefix in ["S/O", "W/O", "D/O", "SO ", "WO ", "DO "]):
                data["consumer_name"] = ", ".join(parts[:2])
                data["consumer_address"] = ", ".join(parts[2:])
            else:
                data["consumer_name"] = parts[0]
                data["consumer_address"] = ", ".join(parts[1:])
        else:
            data["consumer_name"] = name_address
            data["consumer_address"] = ""

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

def fetch_bill_from_pitc(base_url: str, identifier: str, company_name: str) -> Dict[str, Any]:
    """
    Fetches duplicate electricity bill details from the generic PITC bill query page.
    """
    # Remove all non-digits from input
    cleaned_id = re.sub(r'\D', '', identifier)
    
    if len(cleaned_id) == 10:
        is_ref_no = False
    elif len(cleaned_id) == 14:
        is_ref_no = True
    else:
        raise ValueError(f"Invalid identifier format. Please provide a 10-digit Consumer ID or a 14-digit Reference Number for {company_name}.")
        
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": base_url
    }
    
    # Step 1: GET page to initialize the ASP.NET ViewState and tokens
    try:
        r = session.get(base_url, headers=headers, timeout=15)
        r.raise_for_status()
    except requests.RequestException as e:
        raise ConnectionError(f"Failed to connect to {company_name} billing portal: {e}")
        
    soup = BeautifulSoup(r.text, 'html.parser')
    
    try:
        viewstate = soup.find('input', {'name': '__VIEWSTATE'}).get('value')
        viewstate_gen = soup.find('input', {'name': '__VIEWSTATEGENERATOR'}).get('value')
        event_validation = soup.find('input', {'name': '__EVENTVALIDATION'}).get('value')
        req_token = soup.find('input', {'name': '__RequestVerificationToken'}).get('value')
    except (AttributeError, TypeError) as e:
        raise ValueError(f"Could not parse authentication/state tokens from {company_name} portal. The page structure might have changed: {e}")

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
            r = session.post(base_url, headers=headers, data=payload_postback, timeout=15)
            r.raise_for_status()
        except requests.RequestException as e:
            raise ConnectionError(f"Failed during {company_name} search initialization: {e}")
            
        soup = BeautifulSoup(r.text, 'html.parser')
        
        try:
            viewstate = soup.find('input', {'name': '__VIEWSTATE'}).get('value')
            viewstate_gen = soup.find('input', {'name': '__VIEWSTATEGENERATOR'}).get('value')
            event_validation = soup.find('input', {'name': '__EVENTVALIDATION'}).get('value')
            req_token = soup.find('input', {'name': '__RequestVerificationToken'}).get('value')
        except (AttributeError, TypeError) as e:
            raise ValueError(f"Failed to refresh state tokens after selecting Consumer ID mode for {company_name}: {e}")

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
        r = session.post(base_url, headers=headers, data=payload_search, timeout=20)
        r.raise_for_status()
    except requests.RequestException as e:
        raise ConnectionError(f"Failed to query the {company_name} bill: {e}")
        
    # Check if the PITC portal redirected back to index instead of displaying the duplicate bill
    if "/general" not in r.url and "general?" not in r.url:
        soup = BeautifulSoup(r.text, 'html.parser')
        error_msg = soup.find('span', {'id': 'lblinvalidmsg'})
        if error_msg:
            raise ValueError(f"{company_name} search error: {clean_text(error_msg.get_text())}")
        raise ValueError(f"Bill details page was not returned. The provided ID may be invalid or not in the {company_name} system.")
        
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # Check if the page has a "bill-not-found" block
    if soup.find(class_="bill-not-found"):
        raise ValueError(f"Bill not found. The provided ID may be invalid or does not have an active {company_name} bill.")
        
    # Step 4: Parse bill details and return
    return parse_bill_details(soup, cleaned_id)


def fetch_wasa_lahore_bill(account_no: str) -> Dict[str, Any]:
    """
    Fetches WASA Lahore duplicate bill details from cms.wasalhr.pk.
    """
    # Remove non-digits
    cleaned_id = re.sub(r'\D', '', account_no)
    
    if not (8 <= len(cleaned_id) <= 12):
        raise ValueError("Invalid account number format. WASA Lahore account number should be between 8 and 12 digits.")
        
    base_url = "https://cms.wasalhr.pk/DuplicateBill/showBill"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    session = requests.Session()
    try:
        r = session.get(base_url, params={"acctnum": cleaned_id}, headers=headers, verify=False, timeout=20)
        r.raise_for_status()
    except requests.RequestException as e:
        raise ConnectionError(f"Failed to connect to WASA Lahore duplicate bill portal: {e}")
        
    text = r.text
    if "Wrong Account No." in text or "not found" in text.lower():
        raise ValueError("WASA Lahore search error: Wrong Account No. or Bill not found.")
        
    soup = BeautifulSoup(text, 'html.parser')
    
    # Parser helper utilizing table structure & sibling matching
    def get_val(label_regex: str) -> str:
        pattern = re.compile(label_regex, re.IGNORECASE)
        for tag in soup.find_all(['td', 'th', 'span', 'div', 'p', 'b', 'strong', 'label']):
            tag_text = clean_text(tag.get_text())
            if pattern.search(tag_text):
                # Try next sibling tag
                sibling = tag.find_next_sibling()
                if sibling:
                    val = clean_text(sibling.get_text())
                    if val:
                        return val
                # Try parent's next sibling tag (if label is wrapped in strong/span)
                parent = tag.parent
                if parent and parent.name in ['td', 'th', 'div', 'span']:
                    parent_sibling = parent.find_next_sibling()
                    if parent_sibling:
                        val = clean_text(parent_sibling.get_text())
                        if val:
                            return val
        return ""

    data = {
        "queried_id": cleaned_id,
        "consumer_id": cleaned_id,
        "reference_no": cleaned_id,
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
    
    # Search fields using various possible labels
    data["consumer_name"] = get_val(r"consumer\s*name|name\s*of\s*consumer|^name$")
    data["consumer_address"] = get_val(r"consumer\s*address|address")
    data["billing_month"] = get_val(r"billing\s*month|bill\s*month|month")
    data["due_date"] = get_val(r"due\s*date|last\s*date")
    data["payable_within_due_date"] = get_val(r"payable\s*within\s*due\s*date|amount\s*payable|current\s*bill|payable\s*by\s*due")
    data["late_payment_surcharge"] = get_val(r"late\s*payment\s*surcharge|surcharge|late\s*fee")
    data["payable_after_due_date"] = get_val(r"payable\s*after\s*due\s*date|payable\s*after")
    data["tariff"] = get_val(r"tariff|connection\s*type|category")
    data["meter_no"] = get_val(r"meter\s*no|meter\s*number")
    data["units_consumed"] = get_val(r"units\s*consumed|units")
    
    # Clean numeric fields
    for key in ["payable_within_due_date", "late_payment_surcharge", "payable_after_due_date", "units_consumed"]:
        val = data[key]
        if val:
            num_match = re.search(r'[\d,]+(?:\.\d+)?', val)
            if num_match:
                data[key] = num_match.group(0).replace(",", "")
            else:
                data[key] = ""
                
    return data


def fetch_cda_water_bill(consumer_no: str) -> Dict[str, Any]:
    """
    Fetches duplicate CDA water and allied charges bill details from owo.cda.gov.pk.
    """
    cleaned_id = re.sub(r'\D', '', consumer_no)
    if not (6 <= len(cleaned_id) <= 12):
        raise ValueError("Invalid consumer number format. CDA consumer number should be between 6 and 12 digits.")
        
    base_url = "https://owo.cda.gov.pk/duplicatewaterbill.aspx"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": base_url
    }
    
    session = requests.Session()
    
    try:
        r = session.get(base_url, headers=headers, verify=False, timeout=15)
        r.raise_for_status()
    except requests.RequestException as e:
        raise ConnectionError(
            f"Failed to connect to CDA billing portal (https://owo.cda.gov.pk). "
            f"The server might be down for maintenance or offline: {e}"
        )
        
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # Extract ASP.NET state variables
    try:
        viewstate = soup.find('input', {'name': '__VIEWSTATE'}).get('value', '')
        viewstate_gen = soup.find('input', {'name': '__VIEWSTATEGENERATOR'}).get('value', '')
        event_validation = soup.find('input', {'name': '__EVENTVALIDATION'}).get('value', '')
    except (AttributeError, TypeError) as e:
        raise ValueError(
            f"Could not parse ASP.NET state from CDA portal. "
            f"The page structure may have changed: {e}"
        )
        
    # Dynamically locate the Consumer No field and search button
    consumer_field = None
    btn_search = None
    
    for inp in soup.find_all('input'):
        inp_type = (inp.get('type') or '').lower()
        inp_name = inp.get('name') or ''
        inp_id = inp.get('id') or ''
        
        if inp_type in ['text', ''] and not consumer_field:
            if any(k in inp_name.lower() or k in inp_id.lower() for k in ['consumer', 'acc', 'number', 'id', 'txt']):
                consumer_field = inp_name
        
        if inp_type == 'submit' and not btn_search:
            if any(k in inp_name.lower() or k in inp_id.lower() for k in ['search', 'submit', 'btn', 'show', 'print']):
                btn_search = inp_name
                
    # Fallbacks if dynamic detection fails
    if not consumer_field:
        consumer_field = "ctl00$ContentPlaceHolder1$txtConsumerNo"
    if not btn_search:
        btn_search = "ctl00$ContentPlaceHolder1$btnSearch"
        
    payload = {
        "__VIEWSTATE": viewstate,
        "__VIEWSTATEGENERATOR": viewstate_gen,
        "__EVENTVALIDATION": event_validation,
        consumer_field: cleaned_id,
        btn_search: "Search"
    }
    
    # Include other hidden inputs that might be on the page
    for inp in soup.find_all('input', {'type': 'hidden'}):
        name = inp.get('name')
        if name and name not in payload:
            payload[name] = inp.get('value', '')
            
    try:
        r = session.post(base_url, headers=headers, data=payload, verify=False, timeout=20)
        r.raise_for_status()
    except requests.RequestException as e:
        raise ConnectionError(f"Failed to submit query to CDA portal: {e}")
        
    response_text = r.text
    if "not found" in response_text.lower() or "invalid" in response_text.lower():
        raise ValueError("CDA search error: Bill not found or invalid Consumer Number.")
        
    soup = BeautifulSoup(response_text, 'html.parser')
    
    # Parse out values
    def get_val(label_regex: str) -> str:
        pattern = re.compile(label_regex, re.IGNORECASE)
        for tag in soup.find_all(['td', 'th', 'span', 'div', 'p', 'b', 'strong', 'label']):
            tag_text = clean_text(tag.get_text())
            if pattern.search(tag_text):
                # Try next sibling
                sibling = tag.find_next_sibling()
                if sibling:
                    val = clean_text(sibling.get_text())
                    if val:
                        return val
                # Try parent's next sibling
                parent = tag.parent
                if parent and parent.name in ['td', 'th', 'div', 'span']:
                    parent_sibling = parent.find_next_sibling()
                    if parent_sibling:
                        val = clean_text(parent_sibling.get_text())
                        if val:
                            return val
        return ""
        
    data = {
        "queried_id": cleaned_id,
        "consumer_id": cleaned_id,
        "reference_no": cleaned_id,
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
    
    # Try common CDA water bill labels
    data["consumer_name"] = get_val(r"consumer\s*name|name\s*of\s*consumer|^name$")
    data["consumer_address"] = get_val(r"consumer\s*address|address")
    data["billing_month"] = get_val(r"billing\s*month|bill\s*month|month|billing\s*period")
    data["due_date"] = get_val(r"due\s*date|last\s*date")
    data["payable_within_due_date"] = get_val(r"payable\s*within\s*due\s*date|amount\s*payable|current\s*bill|payable\s*by\s*due|amount\s*due")
    data["late_payment_surcharge"] = get_val(r"late\s*payment\s*surcharge|surcharge|late\s*fee|surcharge\s*after\s*due")
    data["payable_after_due_date"] = get_val(r"payable\s*after\s*due\s*date|payable\s*after|gross\s*payable|amount\s*after\s*due")
    data["tariff"] = get_val(r"tariff|connection\s*type|category|billing\s*category")
    data["meter_no"] = get_val(r"meter\s*no|meter\s*number")
    data["units_consumed"] = get_val(r"units\s*consumed|units")
    
    # Clean numeric fields
    for key in ["payable_within_due_date", "late_payment_surcharge", "payable_after_due_date", "units_consumed"]:
        val = data[key]
        if val:
            num_match = re.search(r'[\d,]+(?:\.\d+)?', val)
            if num_match:
                data[key] = num_match.group(0).replace(",", "")
            else:
                data[key] = ""
                
    return data


def fetch_wasa_faisalabad_bill(account_no: str) -> Dict[str, Any]:
    """
    Fetches duplicate WASA Faisalabad duplicate bill details from billingdev.wasafaisalabad.gop.pk.
    """
    cleaned_id = re.sub(r'\D', '', account_no)
    if not (8 <= len(cleaned_id) <= 12):
        raise ValueError("Invalid Account Number format. WASA Faisalabad account number should be between 8 and 12 digits.")
        
    url = f"https://billingdev.wasafaisalabad.gop.pk/BillView/{cleaned_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        r = requests.get(url, headers=headers, verify=False, timeout=15)
        r.raise_for_status()
    except requests.RequestException as e:
        raise ConnectionError(f"Failed to connect to WASA Faisalabad duplicate bill portal: {e}")
        
    text = r.text
    if "no record found" in text.lower() or "not found" in text.lower():
        raise ValueError("WASA Faisalabad search error: Account Number not found or bill not generated.")
        
    soup = BeautifulSoup(text, 'html.parser')
    
    def get_val(label_regex: str) -> str:
        pattern = re.compile(label_regex, re.IGNORECASE)
        for tag in soup.find_all(['td', 'th', 'span', 'div', 'p', 'b', 'strong', 'label']):
            tag_text = clean_text(tag.get_text())
            if pattern.search(tag_text):
                sibling = tag.find_next_sibling()
                if sibling:
                    val = clean_text(sibling.get_text())
                    if val:
                        return val
                parent = tag.parent
                if parent and parent.name in ['td', 'th', 'div', 'span']:
                    parent_sibling = parent.find_next_sibling()
                    if parent_sibling:
                        val = clean_text(parent_sibling.get_text())
                        if val:
                            return val
        return ""
        
    data = {
        "queried_id": cleaned_id,
        "consumer_id": cleaned_id,
        "reference_no": cleaned_id,
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
    
    data["consumer_name"] = get_val(r"consumer\s*name|name\s*of\s*consumer|^name$")
    data["consumer_address"] = get_val(r"consumer\s*address|address")
    data["billing_month"] = get_val(r"billing\s*month|bill\s*month|month|billing\s*period")
    data["due_date"] = get_val(r"due\s*date|last\s*date")
    data["payable_within_due_date"] = get_val(r"payable\s*within\s*due\s*date|amount\s*payable|current\s*bill|payable\s*by\s*due|amount\s*due")
    data["late_payment_surcharge"] = get_val(r"late\s*payment\s*surcharge|surcharge|late\s*fee|surcharge\s*after\s*due")
    data["payable_after_due_date"] = get_val(r"payable\s*after\s*due\s*date|payable\s*after|gross\s*payable|amount\s*after\s*due")
    data["tariff"] = get_val(r"tariff|connection\s*type|category|billing\s*category")
    data["meter_no"] = get_val(r"meter\s*no|meter\s*number")
    data["units_consumed"] = get_val(r"units\s*consumed|units")
    
    # Clean numeric fields
    for key in ["payable_within_due_date", "late_payment_surcharge", "payable_after_due_date", "units_consumed"]:
        val = data[key]
        if val:
            num_match = re.search(r'[\d,]+(?:\.\d+)?', val)
            if num_match:
                data[key] = num_match.group(0).replace(",", "")
            else:
                data[key] = ""
                
    return data


def fetch_wasa_rawalpindi_bill(consumer_no: str) -> Dict[str, Any]:
    """
    Fetches duplicate WASA Rawalpindi bill details from the JSON API.
    """
    cleaned_id = re.sub(r'\D', '', consumer_no)
    if not (6 <= len(cleaned_id) <= 12):
        raise ValueError("Invalid Consumer Number format. WASA Rawalpindi consumer number should be between 6 and 12 digits.")
        
    url = f"https://wasarwp.gop.pk/api/search_bill.php?consumer_no={cleaned_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://wasarwp.gop.pk/"
    }
    
    try:
        r = requests.get(url, headers=headers, verify=False, timeout=15)
        if r.status_code == 404:
            try:
                resp = r.json()
                msg = resp.get("message")
                if msg:
                    raise ValueError(f"WASA Rawalpindi search error: {msg}")
            except Exception as ex:
                if isinstance(ex, ValueError):
                    raise ex
            raise ValueError("WASA Rawalpindi search error: Consumer Number not found.")
            
        r.raise_for_status()
        resp = r.json()
    except requests.RequestException as e:
        raise ConnectionError(f"Failed to connect to WASA Rawalpindi duplicate bill portal: {e}")
    except ValueError as e:
        raise e
        
    if not resp.get("success"):
        raise ValueError(f"WASA Rawalpindi search error: {resp.get('message', 'Bill not found')}")
        
    bill = resp.get("bill", {})
    
    data = {
        "queried_id": cleaned_id,
        "consumer_id": bill.get("wasa_no") or bill.get("wasaNo") or cleaned_id,
        "reference_no": bill.get("wasa_no") or bill.get("wasaNo") or cleaned_id,
        "consumer_name": clean_text(bill.get("name")),
        "consumer_address": clean_text(bill.get("address")),
        "billing_month": clean_text(bill.get("session_code") or bill.get("sessionCode")),
        "due_date": clean_text(bill.get("due_date") or bill.get("dueDate")),
        "payable_within_due_date": clean_text(str(bill.get("total_bill") or bill.get("totalBill") or "")),
        "late_payment_surcharge": clean_text(str(bill.get("surcharge") or "")),
        "payable_after_due_date": clean_text(str(bill.get("payable_after_due") or bill.get("payableAfterDue") or "")),
        "units_consumed": clean_text(str(bill.get("units_consumed") or bill.get("unitsConsumed") or bill.get("units") or "")),
        "meter_no": "",
        "connection_date": clean_text(bill.get("con_date") or bill.get("conDate")),
        "tariff": clean_text(bill.get("connectionType") or bill.get("cat_code") or bill.get("catCode")),
        "load": ""
    }
    
    # Clean numeric fields
    for key in ["payable_within_due_date", "late_payment_surcharge", "payable_after_due_date", "units_consumed"]:
        val = data[key]
        if val:
            num_match = re.search(r'[\d,]+(?:\.\d+)?', val)
            if num_match:
                data[key] = num_match.group(0).replace(",", "")
            else:
                data[key] = ""
                
    return data


def fetch_wasa_hyderabad_bill(consumer_no: str) -> Dict[str, Any]:
    """
    Fetches duplicate WASA Hyderabad bill details from Laravel/Inertia endpoint.
    """
    import urllib.parse
    import json
    
    cleaned_id = re.sub(r'\D', '', consumer_no)
    if not (6 <= len(cleaned_id) <= 12):
        raise ValueError("Invalid Reference Number format. WASA Hyderabad consumer number should be between 6 and 12 digits.")
        
    base_url = "https://bill.hwsc.gos.pk/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    session = requests.Session()
    
    # Step 1: GET main page to retrieve Inertia Version and CSRF Token
    try:
        r = session.get(base_url, headers=headers, verify=False, timeout=15)
        r.raise_for_status()
    except requests.RequestException as e:
        raise ConnectionError(f"Failed to connect to WASA Hyderabad duplicate bill portal: {e}")
        
    soup = BeautifulSoup(r.text, 'html.parser')
    app_div = soup.find(id='app') or soup.find(attrs={"data-page": True})
    
    inertia_version = "8c42234b07a22ef8845d290b1fbda0a2" # default fallback
    if app_div and app_div.get('data-page'):
        try:
            page_data = json.loads(app_div.get('data-page'))
            inertia_version = page_data.get('version', inertia_version)
        except Exception:
            pass
            
    token = urllib.parse.unquote(session.cookies.get('XSRF-TOKEN', ''))
    if not token:
        raise ValueError("Could not retrieve session token from WASA Hyderabad portal.")
        
    # Step 2: POST to search endpoint
    search_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": base_url,
        "X-XSRF-TOKEN": token,
        "X-Inertia": "true",
        "X-Inertia-Version": inertia_version,
        "Content-Type": "application/json"
    }
    
    payload = {
        "reference": cleaned_id,
        "recaptcha_token": "dummy_token",
        "website": ""
    }
    
    try:
        r = session.post(f"{base_url}search", json=payload, headers=search_headers, verify=False, timeout=15)
        
        # Handle 404 cleanly
        if r.status_code == 404:
            try:
                err_data = r.json()
                msg = err_data.get("message")
                if msg:
                    raise ValueError(f"WASA Hyderabad search error: {msg}")
            except Exception as ex:
                if isinstance(ex, ValueError):
                    raise ex
            raise ValueError("WASA Hyderabad search error: Reference Number not found.")
            
        r.raise_for_status()
        resp = r.json()
    except requests.RequestException as e:
        raise ConnectionError(f"Failed to submit query to WASA Hyderabad portal: {e}")
    except ValueError as e:
        # Re-raise standard value errors
        raise e
        
    props = resp.get("props", {})
    errors = props.get("errors", {})
    if errors:
        error_msg = next(iter(errors.values()))
        raise ValueError(f"WASA Hyderabad search error: {error_msg}")
        
    invoices = props.get("invoices", [])
    if not invoices:
        raise ValueError("WASA Hyderabad search error: No bills found for this connection.")
        
    # Retrieve the latest invoice (first in the array)
    latest = invoices[0]
    
    data = {
        "queried_id": cleaned_id,
        "consumer_id": props.get("new_reference") or props.get("old_reference") or cleaned_id,
        "reference_no": props.get("old_reference") or props.get("new_reference") or cleaned_id,
        "consumer_name": clean_text(props.get("consumer_name")),
        "consumer_address": clean_text(props.get("address")),
        "billing_month": clean_text(latest.get("billing_month")),
        "due_date": clean_text(latest.get("due_date")),
        "payable_within_due_date": clean_text(str(latest.get("amount") or "")),
        "late_payment_surcharge": "",
        "payable_after_due_date": "",
        "units_consumed": "",
        "meter_no": "",
        "connection_date": "",
        "tariff": "",
        "load": ""
    }
    
    # Clean numeric fields
    for key in ["payable_within_due_date", "late_payment_surcharge", "payable_after_due_date", "units_consumed"]:
        val = data[key]
        if val:
            num_match = re.search(r'[\d,]+(?:\.\d+)?', val)
            if num_match:
                data[key] = num_match.group(0).replace(",", "")
            else:
                data[key] = ""
                
    return data



