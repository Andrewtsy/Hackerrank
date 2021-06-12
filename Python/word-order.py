from collections import Counter

lst = [str(input().strip()) for i in range(int(input()))]
print(str(len(Counter(lst))), '\n', *[str(i) + ' ' for i in Counter(lst).values()], sep='')
