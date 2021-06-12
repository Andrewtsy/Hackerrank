# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

if __name__ == '__main__':
    N = int(input())
    d = deque()
    def val_unpack(*args):
        fun = args[0]
        if len(args) == 2:
            val = args[1]
        else:
            val = ''
        return (fun, val)
        
    for i in range(N):
        eval('d.{}({})'.format(*val_unpack(*input().split())))
    print(*d, end='')
