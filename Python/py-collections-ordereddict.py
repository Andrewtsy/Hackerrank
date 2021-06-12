# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict, defaultdict
import re

def splitter(string):
    name = re.search('[A-Z\s]+', string).group(0)[:-1]
    price = re.search('[0-9]+', string).group(0)
    return name, price
    
if __name__ == '__main__':
    ordict = OrderedDict()
    N = int(input())
    for i in range(N):
        name, price = splitter(input())
        if not name in ordict.keys():
            ordict[name] = int(price)
        else:
            ordict[name] += int(price)
    for k, v in ordict.items():
        print(k + ' ' + str(v))     
            
