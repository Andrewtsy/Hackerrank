

# Complete the solve function below.
def solve(s):
    inp = s.split() 
    out = ''
    count = True
    for i in s:
        if count == True:
            out += i.upper()
        else:
            out += i        
        if i == ' ':
            count = True
        else:
            count = False
    return out

