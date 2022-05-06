import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-d\d\d\d')
mo = phoneNumRegex.search ('call me at 415-555-191 tommorow, or at 15-555-9999')
print (mo.group())
