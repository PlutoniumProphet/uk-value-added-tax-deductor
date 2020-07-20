# uk-value-added-tax-deductor
Simple tool for removing the amount of UK VAT applied to a total receipt. 
Over-engineered to explore Python's ArgParse library in a little detail. 



usage: VATDeductor [-h] [--version] [--rate [RATE]] [--verbose] T

Displays the VAT deductable from a total receipt value

positional arguments:
  T              amount of TOTAL receipt value for processing

optional arguments:
  -h, --help     show this help message and exit
  --version      show program's version number and exit
  --rate [RATE]  enter VAT rate as a decimal. Default is 1.2
  --verbose      displays Total Amount, VAT deductable & pretax values
