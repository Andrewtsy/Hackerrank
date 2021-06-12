from collections import Counter

def main(s):
    Count = Counter([i for i in s.strip()])
    Count = sorted(Count.items(), key = lambda x: (x[1], -ord(x[0])), reverse=True)[0:3]
    print(*list(map(lambda x: f'{x[0]} {x[1]}', Count)), sep='\n')


if __name__ == '__main__':
    s = input()
    main(s)
