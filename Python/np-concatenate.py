import numpy

N, M, P = list(map(int, input().strip().split()))

NP = numpy.array([list(list(map(int, input().split()))) for i in range(N)])
MP = numpy.array([list(list(map(int, input().split()))) for i in range(M)])
print(numpy.concatenate((NP, MP), axis=0))
