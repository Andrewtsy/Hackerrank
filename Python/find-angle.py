# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    
    theta = math.atan(x/y)
    theta = theta * 180 / math.pi
    theta = round(theta)
    degree_sign = u'\N{DEGREE SIGN}'
    print(str(theta) + degree_sign)
