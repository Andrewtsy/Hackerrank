# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input()
set1 = set([i for i in input().split()])
n = input()
set2 = set([i for i in input().split()])

print(len(set1 ^ set2))
