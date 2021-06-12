import sys
import numpy as np

arr = np.array([list(map(int, sys.stdin.readline().split())) for i in range(int(sys.stdin.readline().split()[0]))])

sys.stdout.write(str(np.mean(arr, axis=1)) + '\n' + str(np.var(arr, axis=0)) + '\n' + str(round(np.std(arr, axis=None), 11)))
