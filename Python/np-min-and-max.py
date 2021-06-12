import sys
import numpy as np
np.set_printoptions(legacy='1.13')

arr = np.array([list(map(int, sys.stdin.readline().split())) for i in range(int(sys.stdin.readline().split()[0]))])

sys.stdout.write(str(np.max(np.min(arr, axis=1))))
