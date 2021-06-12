# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
s = set([int(i) for i in input().split()])

N = int(input())
for i in range(N):
    fun, l = input().split()
    ns = set([int(i) for i in input().split()])
    getattr(s, fun)(ns)
print(sum(s))
