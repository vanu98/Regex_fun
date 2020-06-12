#pan card validity
import re

pan_no = input('Enter PAN number: ')

output = re.match('((([a-zA-Z]{5})\\d{4})[a-zA-Z]{1})', pan_no)

if output:
	print('Valid PAN number')
else:
	print('Not Valid PAN number')