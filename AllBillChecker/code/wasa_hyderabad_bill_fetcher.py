#!/usr/bin/env python3
"""
WASA Hyderabad (HWSC) Duplicate Bill Fetcher
Fetches water and sewerage bill details from Hyderabad Water Supply & Sewerage Corporation (HWSC)
using a 6-digit to 12-digit Reference Number / Consumer Number.
"""

import sys
import argparse
import json
from bill_utility import fetch_wasa_hyderabad_bill

def main():
    parser = argparse.ArgumentParser(
        description="Connects to HWSC duplicate bill portal and fetches details using Reference/Consumer Number.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python wasa_hyderabad_bill_fetcher.py --id 12345678901
  python wasa_hyderabad_bill_fetcher.py --id 12345678901 --json
"""
    )
    parser.add_argument(
        "-i", "--id",
        required=True,
        help="The 6-to-12-digit Reference/Consumer Number."
    )
    parser.add_argument(
        "-j", "--json",
        action="store_true",
        help="Output the bill details in raw JSON format (useful for piping/scripting)."
    )

    args = parser.parse_args()

    try:
        bill_data = fetch_wasa_hyderabad_bill(args.id)
        
        if args.json:
            print(json.dumps(bill_data, indent=2))
        else:
            print("\n" + "="*50)
            print("       WASA HYDERABAD (HWSC) BILL DETAILS SUMMARY")
            print("="*50)
            print(f"Queried ID:             {bill_data['queried_id']}")
            print(f"Consumer ID (Cust ID):  {bill_data['consumer_id'] or 'N/A'}")
            print(f"Reference Number:       {bill_data['reference_no'] or 'N/A'}")
            print(f"Billing Month:          {bill_data['billing_month'] or 'N/A'}")
            print(f"Consumer Name:          {bill_data['consumer_name'] or 'N/A'}")
            print(f"Consumer Address:       {bill_data['consumer_address'] or 'N/A'}")
            print(f"Tariff / Category:      {bill_data['tariff'] or 'N/A'}")
            print(f"Units Consumed:         {bill_data['units_consumed'] or 'N/A'}")
            print(f"Meter Number:           {bill_data['meter_no'] or 'N/A'}")
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
