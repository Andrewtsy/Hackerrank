import numpy

numpy.set_printoptions(legacy='1.13')

dim = tuple(map(int, input().split()))
print(eval(f'numpy.eye{dim}'))
