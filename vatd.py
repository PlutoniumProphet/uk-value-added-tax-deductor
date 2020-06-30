""" Simple tool for removing the amount of UK VAT applied to a total receipt.
    Over-enginneered to explore Python's ArgParse library in detail."""

import argparse


parser = argparse.ArgumentParser(
    prog='VAT Deductor',
    description='Displays the VAT deductable from a total receipt value')
parser.add_argument(
    '--version',
    action='version',
    version='%(prog)s 1.0')
parser.add_argument(
    '--rate',
    type=float,
    action='store',
    nargs='?',
    default='1.2',
    help='enter VAT rate as a decimal. Default is 1.2')
parser.add_argument(
    '-v',
    '--verbose',
    action='store_true',
    help='displays Total Amount, VAT deductable & pretax values')
parser.add_argument(
    'total',
    metavar='T',
    type=float,
    action='store',
    help='amount of TOTAL receipt value for processing')

args = parser.parse_args()

net_value = round(args.total / args.rate, 2)
refund_vat = round(args.total - net_value, 2)

if args.verbose:
    print(f"""
Total Receipt:  £{args.total}
Net Value:      £{net_value}
Deductable VAT: £{refund_vat}
          """)
else:
    print(f"Deductable VAT: £{refund_vat}")
