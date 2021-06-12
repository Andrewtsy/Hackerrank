import numpy

arr = numpy.array([input().strip().split() for i in range(int(input().split()[0]))], int)
print(numpy.transpose(arr), arr.flatten(), sep='\n')
