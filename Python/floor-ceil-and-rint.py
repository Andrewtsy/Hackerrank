import sys
import numpy as np
np.set_printoptions(legacy='1.13')

arr = np.array(sys.stdin.readline().split(), float)

sys.stdout.write(str(np.floor(arr)) + '\n' + str(np.ceil(arr)) + '\n' + str(np.rint(arr)))
