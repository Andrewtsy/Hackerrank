# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

if __name__ == '__main__':
    N = int(input())
    
    spreadsheet = namedtuple('spreadsheet', input().split())
    d = {}
    
    s = 0
    
    for i in range(N):
        d[i] = spreadsheet._make(input().split())
        s += int(d[i].MARKS)
        
    print(s/N)
