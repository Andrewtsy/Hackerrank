# Enter your code here. Read input from STDIN. Print output to STDOUT

n1 = int(input())
s1 = set([int(i) for i in input().split()])

n2 = int(input())
s2 = set([int(i) for i in input().split()])

print(len(s1 | s2))
