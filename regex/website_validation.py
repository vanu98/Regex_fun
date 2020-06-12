#link validity checker
import re

link = input('Enter website link: ')

output =re.match('^(http|https|ftp)\:[\/]{2}[a-zA-Z0-9]+\.(com|co|org|in)', link)

if output:
	print('Valid')
else:
	print('Not Valid')
