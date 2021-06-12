if __name__ == '__main__':
    import re
    p1 = re.compile('[a-z]+')
    p2 = re.compile('[0-9]+')
    N = int(input())
    arr = []
    for i in range(N):
        do = input()
        funct = p1.findall(do)[0]
        try:
            param1 = p2.findall(do)[0]
        except:
            param1 = ''
        try:
            param2 = ', ' + p2.findall(do)[1]
        except:
            param2 = ''
        try:
            eval('arr.' + str(funct) + '(' + str(param1) + str(param2) + ')')
        except:
            print(arr)
