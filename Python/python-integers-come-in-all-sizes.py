# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

a, b, c, d = map(int, sys.stdin)
a, b, c, d = map(int, [a, b, c, d])
sys.stdout.write(str(pow(a, b) + pow(c, d)))
