# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

# for i in sys.stdin.read():
#     sys.stdout.write(i.strip())

# a, b, m = map(int, [line.strip() for line in sys.stdin.read() if line != '\n'])
# sys.stdout.write('\n'.join([str(pow(a, b)), str(pow(a, b, m))]))

a = int(input())
b = int(input())
m = int(input())

print(pow(a, b), pow(a, b, m), sep='\n')
