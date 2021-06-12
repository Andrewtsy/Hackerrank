n = int(input())
s = set(map(int, input().split()))

N = int(input())

def fun(string):
    com = string.split()
    if len(com) == 2:
        com = '.{}({})'.format(com[0], com[1])
    else:
        com = '.{}()'.format(com[0])
    return com
    
for i in range(N):
    com = 's' + fun(input())
    eval(com)

print(sum(s))
