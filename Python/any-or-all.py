# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

N = sys.stdin.readline()
lst = [i for i in sys.stdin.read().split()]
print(all([int(i) > 0 for i in lst]) and any([i[::-1] == i for i in lst]))
