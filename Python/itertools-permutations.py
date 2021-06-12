# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

if __name__ == '__main__':
    inp = input()
    string = inp.split()[0]
    k = inp.split()[1]
    
    stdout = []
    
    for i in list(permutations(string, int(k))):
        out = ''
        for j in i:
            out += j
        stdout.append(out)
        
    stdout.sort()
    for i in stdout:
        print(i)
