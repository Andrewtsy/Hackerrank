import numpy

import sys
import numpy as np

class fun():
    def __init__(self, arr, typ=float):
        self.arr = list(map(typ, arr))
    def polyval(self, x):
        return np.polyval(self.arr, x)

arr = fun(sys.stdin.readline().split())
x = int(sys.stdin.readline())

sys.stdout.write(str(arr.polyval(x)))
