import sys
import numpy as np

N = int(sys.stdin.readline().split()[0])
A = np.array([list(map(int, sys.stdin.readline().split())) for i in range(N)])
B = np.array([list(map(int, sys.stdin.readline().split())) for i in range(N)])

M =np.array([[np.dot(A[i,:], B[:,j]) for j in range(N)] for i in range(N)])

print(M)
