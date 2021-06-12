# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

N = int(sys.stdin.readline())
for i in range(N):
    n1, s1, n2, s2 = int(sys.stdin.readline()), set(sys.stdin.readline().split()), int(sys.stdin.readline()), set(sys.stdin.readline().split())
    if s1 - s2 == set() and not s2 - s1 == set():
        sys.stdout.write('True \n')
    else:
        sys.stdout.write('False \n')
