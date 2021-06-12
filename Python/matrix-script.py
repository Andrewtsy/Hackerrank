import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append([i for i in matrix_item])

string = ''

p = re.compile(r'\w(\W.)\w')

for column in range(m):
    for row in range(n):
        string += matrix[row][column]
        
print(re.sub(r'(\w)\W+(\w)', r'\1 \2', string))
