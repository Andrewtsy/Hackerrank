# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    M = int(input())
    set1 = set(map(int, input().split()))
    N = int(input())
    set2 = set(map(int, input().split()))
    
    myset = set1.difference(set2) 
    myset.update((set2.difference(set1)))
    myset = sorted(myset)
    
    for i in myset:
        print(i)
    
    
