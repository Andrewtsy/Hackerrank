import re

def subbing(match):
    if match.group(0) == '&&':
        return 'and'
    if match.group(0) == '||':
        return 'or'

for i in range(int(input())):
    print(re.sub(r'(?<= )(\&\&|\|\|)(?= )', subbing, input()))
