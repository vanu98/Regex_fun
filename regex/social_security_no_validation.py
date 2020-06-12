#social security number validity
import re
ssn = input('Enter Social security no: ')

output = re.match('[0-9]{3}\-[0-9]{2}\-[0-9]{4}', ssn)

if output:
	print('Valid social securrity number')
else:
	print('Not a Valid social security number')