#!/bin/python3

import math
import os
import random
import re
import sys
from dateutil import parser
import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    t1, t2 = map(parser.parse, [t1, t2])
    return int(abs(t1 - t2).total_seconds())
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(str(delta) + '\n')

    fptr.close()
