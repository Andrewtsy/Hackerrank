# Enter your code here. Read input from STDIN. Print output to STDOUT

stdin = input()
N, M = int(stdin.split()[0]),int( stdin.split()[1])

des = '.|.'
side = int((N - 1) / 2)

for i in range(side):
    print((des * (2 * i + 1)).center(M, '-'))
print('WELCOME'.center(M, '-'))
for i in range (side):
    print((des * (side * 2 - (2 * i + 1))).center(M, '-'))
