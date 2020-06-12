#password cmatcher
import re

password = input('Enter your password: \n')
print('password should have minimum 8 characters \nAtleast one uppercase\nAtleast one lowercase \nAtleast one digit\n')

output = re.match('^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$', password)
if output:
	print('Valid')
else:
	print('Not Valid')