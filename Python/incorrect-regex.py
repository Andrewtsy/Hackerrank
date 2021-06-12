# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

if __name__ == '__main__':
    def isvalid(reg):
        try:
            re.compile(reg)
        except:
            print(False)
        else:
            print(True)
            
    n = int(input())
    for i in range(n):
        isvalid(str(input()))
