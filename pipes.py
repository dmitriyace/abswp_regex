import re

heroregex=re.compile(r'Tina|Mina')
mo1 = heroregex.search('Tina and f Mina')
print(mo1.group())