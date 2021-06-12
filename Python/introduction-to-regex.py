# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    try:
        print(bool(float(input())))
    except:
        print(False)
