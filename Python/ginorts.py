import re

S = input().strip()

U, l , od, ed = re.findall('[A-Z]', S), re.findall('[a-z]', S), re.findall('[1,3,5,7,9]', S), re.findall('[0,2,4,6,8]', S)
U.sort(), l.sort(), od.sort(), ed.sort()

print(*l, *U, *od, *ed, sep='')
