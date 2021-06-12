if __name__ == '__main__':
    s = input()
    s = list(s)
    output = [False, False, False, False, False]
    for i in s:
        if i.isalnum():
            output[0] = True
        if i.isalpha():
            output[1] = True
        if i.isdigit():
            output[2] = True
        if i.islower():
            output[3] = True
        if i.isupper():
            output[4] = True
    for i in output:
        print(i)
