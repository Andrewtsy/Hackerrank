if __name__ == '__main__':
    ranking = {}
    def sndsm(lst):
        lst = list(set(lst))
        lst.sort()
        return lst[1]
    def get_keys(dic, val):
        keys = []
        for k, v in dic.items():
            if v == val:
                keys.append(k)
        return keys
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        ranking[name] = score
        
    smallest = sndsm(list(ranking.values()))
    results = get_keys(ranking, smallest)
    results.sort()
    
    print(*results, sep='\n')
