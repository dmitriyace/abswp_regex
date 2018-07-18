import re

phNumRegex = re.compile(r'(\d{3})(-)?(\d{3}(-)?\d{4})')
matchobj = phNumRegex.findall('rjkkjeakjg ekjkj 123-245-5432, 493432-3454')
# print('phnum found: '+matchobj.group())
print(matchobj)