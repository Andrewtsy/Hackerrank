if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lst = list(arr)
    winner = max(lst)
    maximum = winner
    while maximum == winner:
        lst.remove(max(lst))
        maximum = max(lst)
    print(maximum)
