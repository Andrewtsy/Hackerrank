string = input() + 'd'

temp = None
num = 0
run_once = 0
out = []

for i in string:  
    if i == temp:
        num += 1
    else:
        num += 1
        if not run_once == 0: 
            print(str((num, int(temp))), end=' ')
        run_once = 1
        num = 0
        temp = i
print()
