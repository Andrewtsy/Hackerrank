# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import phase
import re

if __name__ == '__main__':
    inp = input()
    x = int(re.findall('^[^0-9]*[0-9]+', inp)[0])
    y = int(re.findall('[^0-9][0-9]+', inp)[-1])

    print(abs(complex(x, y)))
    print(phase(complex(x, y)))
