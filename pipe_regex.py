import re

batRegex = re.compile(r'Bat(man|mob|car|bat)')
mo = batRegex.findall('Batcar lost the wheel egjjnr Batman serjjn Batmob dr Batbat')
print(mo)