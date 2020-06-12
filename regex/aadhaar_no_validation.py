#social security number validity
import re
aadhaar = input('Enter aadhaar no: ')

output = re.match('[0-9]{4}\-[0-9]{4}\-[0-9]{4}', aadhaar)

if output:
	print('Valid aadhaar number')
else:
	print('Not a Valid aadhaar number')