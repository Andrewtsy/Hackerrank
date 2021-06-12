# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import email.utils

p = re.compile(r'^([a-zA-Z][\w._-]+)@([a-zA-Z]+)\.([A-Za-z]{1,3})$')
for i in range(int(input())):
    nm, em = email.utils.parseaddr(input())
    if p.match(em):
        print(f'{nm} <{em}>')

# <[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>
