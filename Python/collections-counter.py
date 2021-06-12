from collections import Counter

if __name__ == '__main__':
    X = int(input())
    lst = input().split()
    N = int(input())
    prices = {}
    customers = []
    rev = 0
    
    def dictionary(dic, k , v):
        if not k in dic.keys():
            dic[k] = [v]
        else:
            dic[k].append(v)
    
    for i in range(N):
        inp = input().split()
        dictionary(prices, inp[0], int(inp[1]))
        customers.append(inp[0])
    
    customers = Counter(customers)
    counter = Counter(lst)
    
    for k, v in customers.items():
        for i in range(v):
            if i < counter[k]:
                rev += prices[k][i]
    
    print(rev)
