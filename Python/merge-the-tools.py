def merge_the_tools(string, k):
    length = k
    num = int(len(string) / k)
    for i in range(num):
        sli = string[i*k:(i+1)*k]
        out = ''
        for j in sli:
            if j not in out:
                out += j
        print(out)

