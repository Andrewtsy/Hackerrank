def wrapper(f):
    def fun(l):
        lst = [('+91 ' + str(i)[-10:-5] + ' ' + str(i)[-5:]) for i in l]
        return f(lst)
    return fun

