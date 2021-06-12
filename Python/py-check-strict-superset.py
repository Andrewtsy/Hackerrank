S = set(input().split())
for i in range(int(input())):
    s = set(input().split())
    if not S.intersection(s) == s or not bool(S - s):
        print(False)
        exit()
print(True)
