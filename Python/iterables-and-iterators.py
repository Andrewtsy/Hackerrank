from itertools import combinations

N = int(input())
lst = input().split()
K = int(input())

combs = list(combinations(lst, K))
print(round(len([i for i in combs if 'a' in i]) / len(combs), 4))
