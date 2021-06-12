import numpy as np

N = int(input())
arr = np.array([list(map(float, input().split())) for i in range(N)])

print(round(np.linalg.det(arr), 2))
