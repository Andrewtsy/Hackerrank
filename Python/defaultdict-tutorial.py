# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

if __name__ == '__main__':
    inp = input().split()
    n, m = int(inp[0]), int(inp[1])
    A, B = [], []
    for i in range(n):
        A.append(input())
    for i in range(m):
        B.append(input())
    
    d = defaultdict(list)
    
    for i in enumerate(B):
        for j in enumerate(A):
            if i[1] == j[1]:
                    d[i[0]].append(j[0] + 1)
        if d[i[0]] == []:
            d[i[0]].append('-1')
    
    for v in d.values():
        print(*v)      
