import sys
import numpy as np

N, M = map(int, sys.stdin.readline().split())
A, B = [], []
for i in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))
for i in range(N):
    B.append(list(map(int, sys.stdin.readline().split())))
A = np.array(A)
B = np.array(B)
sys.stdout.write(str(A + B) + '\n')
sys.stdout.write(str(A - B) + '\n')
sys.stdout.write(str(A * B) + '\n')
sys.stdout.write(str(A // B) + '\n')
sys.stdout.write(str(A % B) + '\n')
sys.stdout.write(str(A ** B) + '\n')
