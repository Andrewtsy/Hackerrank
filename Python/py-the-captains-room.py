# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from collections import defaultdict

K = int(sys.stdin.readline())
rooms = list(sys.stdin.readline().split())
d = defaultdict(int)

for i in rooms:
    d[str(i)] += 1

for k, v in d.items():
    if v == 1:
        sys.stdout.write(k)
