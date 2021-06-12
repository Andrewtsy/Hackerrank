import numpy as np

A, B = list(map(lambda x: np.array(input().split(), int), range(2)))
print(np.inner(A, B), np.outer(A, B), sep='\n')
