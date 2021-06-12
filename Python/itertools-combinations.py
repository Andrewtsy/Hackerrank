# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

if __name__ == '__main__':
    S, k = input().split()
    k = int(k)
    S = [i for i in S]
    S.sort()
    stdout = []
    for i in range(k):
        for j in list(combinations(S, i + 1)):
            n = ''
            for l in j:
                n += l
            stdout.append(n)
    for m in stdout:
        print(m)
