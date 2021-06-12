# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

a, b = map(int, sys.stdin.read().split())

print(a//b, a%b, divmod(a,b), sep='\n')
