# Enter your code here. Read input from STDIN. Print output to STDOUT

N, X = map(int, input().split())

lst = list()

for i in range(X):
    lst.append((map(float, input().split())))

[print(round(sum(i) / len(i), 1)) for i in zip(*lst)]
