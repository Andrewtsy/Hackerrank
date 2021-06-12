def print_rangoli(size):
    lst = [i for i in reversed(range(1, size))] + [0] + [i for i in range(1, size)]
    length = size * 4 - 3
    def add(i):
        return int(i + 97)
    def fun(i):
        return str(chr(i))
    lst = list(map(add, lst))
    lst = list(map(fun, lst))
    for i in range(1, size+1):
        print('-'.join(list(lst[0:i-1]) + list(lst[-i:])).center(length, '-'))
    for i in reversed(range(1, size)):
        print('-'.join(list(lst[0:i-1]) + list(lst[-i:])).center(length, '-'))
    

