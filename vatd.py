""" Simple tool for removing the amount of UK VAT applied to a total receipt.
    Over-enginneered to explore Python's ArgParse library in detail."""

import argparse

parser = argparse.ArgumentParser(prog='VAT Deductor',
    description='Displays the VAT deductable from a total receipt value')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
parser.add_argument('--rate', type=float, action='store',
                    nargs='?', default='1.2',
                help='enter VAT rate as a decimal. Default is 1.2')
parser.add_argument('-v', '--verbose', action='store_true',
                help='displays Total Amount, VAT deductable & pretax values')
parser.add_argument('Total', metavar='T', type=float, action='store',
                help='amount of TOTAL receipt value for processing')


parser.parse_args()

#VAT_RATE = 1.20


#def calc():
 #   try:
  #      receipt_value = input("Enter receipt value: ")
   #     receipt_value = float(receipt_value)
    #    net_value = float(receipt_value) / VAT_RATE
     #   refund_vat = round(float(receipt_value) - net_value, 2)
      #  print(refund_vat)
       # if input("Run again? ") == "y":
        #    calc()
       # else:
        #    print("Bye!")
    #except ValueError:
     #   print("You can only enter numbers!")
      #  calc()

#calc()
