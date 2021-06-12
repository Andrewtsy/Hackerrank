

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    for child in elem:
        depth(child, level)
    if level > maxdepth:
        maxdepth = level

