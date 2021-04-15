import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
google.com
!@#$%^^&**(())&{}><?
'''

# \s - whitespace tab and newline

pattern = re.compile(r'abc')
matches = pattern.finditer(text_to_search)

# for match in matches:
    # print(match)

m = re.match(r'def', text_to_search)    # only matches beginning
s = re.search(r'def', text_to_search)   # matches anywhere in the string
print(m)
print(s)

