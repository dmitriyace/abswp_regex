import re

batRegex=re.compile(r'bat(wo)*man')
mo1 = batRegex.search('adventures of batman')
print(mo1.group())
mo2 = batRegex.search('adventures of batwowoman')
print(mo2.group())