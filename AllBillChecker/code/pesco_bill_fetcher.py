#!/usr/bin/env python3
"""
PESCO Duplicate Bill Fetcher
Fetches electricity bill details from Peshawar Electric Supply Company (PESCO) 
using a 10-digit Customer ID (Consumer ID) or a 14-digit Reference Number.
"""

import sys
import argparse
import json
from bill_utility import fetch_bill_from_pitc

# Base PITC URL for PESCO duplicate bills
PESCO_BILL_URL = "https://bill.pitc.com.pk/pescobill"

def fetch_pesco_bill(identifier: str) -> dict:
    """
    Fetches the duplicate PESCO bill details using either:
    - 10-digit Customer ID / Consumer ID
    - 14-digit Reference Number
    """
    return fetch_bill_from_pitc(PESCO_BILL_URL, identifier, "PESCO")

def main():
    parser = argparse.ArgumentParser(
        description="Connects to PESCO and fetches details of the duplicate bill using Consumer ID or Reference Number.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python pesco_bill_fetcher.py --id 1234567890
  python pesco_bill_fetcher.py --id 01123456789012 --json
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
        bill_data = fetch_pesco_bill(args.id)
        
        if args.json:
            print(json.dumps(bill_data, indent=2))
        else:
            print("\n" + "="*50)
            print("         PESCO BILL DETAILS SUMMARY")
            print("="*50)
            print(f"Queried ID:             {bill_data['queried_id']}")
            print(f"Consumer ID (Cust ID):  {bill_data['consumer_id'] or 'N/A'}")
            print(f"Reference Number:       {bill_data['reference_no'] or 'N/A'}")
            print(f"Billing Month:          {bill_data['billing_month'] or 'N/A'}")
            print(f"Consumer Name:          {bill_data['consumer_name'] or 'N/A'}")
            print(f"Consumer Address:       {bill_data['consumer_address'] or 'N/A'}")
            print(f"Tariff / Sanc. Load:    {bill_data['tariff'] or 'N/A'} / {bill_data['load'] or 'N/A'}")
            print(f"Units Consumed:         {bill_data['units_consumed'] or 'N/A'} kWh")
            print(f"Connection Date:        {bill_data['connection_date'] or 'N/A'}")
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
