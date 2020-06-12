#passpot number validity
import re

passport_no = input('Enter Passport number: ')

output = re.match('(([a-zA-Z]{1})\\d{7})', passport_no)

if output:
	print('Valid Passport number')
else:
	print('Not Valid Passport number')