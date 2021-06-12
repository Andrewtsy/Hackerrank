# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

one = input().split()
two = input().split()
one = map(int, one)
two = map(int, two)
print(*list(product(one, two)))
