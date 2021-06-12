import sys
import re

p1 = re.compile(r'[A-Z].*?[A-Z]')
p2 = re.compile(r'[0-9].*?[0-9]+?.*?[0-9]')
p3 = re.compile(r'^\w{10}')
p4 = re.compile(r'(.).*?\1')

for i in range(int(sys.stdin.readline())):
    ele = input()
    if p1.search(ele) and p2.search(ele) and p3.search(ele) and not p4.search(ele):
        print('Valid')
    else:
        print('Invalid')
