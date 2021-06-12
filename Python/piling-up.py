from collections import deque

for i in range(int(input())):
    Works = 'Yes'
    n = int(input())
    d = deque([int(i) for i in input().strip().split()])
    stack = [None]
    for j in range(n):
        if d[0] >= d[-1]:
            if stack[-1] == None or d[0] <= stack[-1]:
                stack.append(d.popleft())
            else:
                Works = 'No'
                print(Works)
                break
        else:
            if stack[-1] == None or d[-1] <= stack[-1]:
                stack.append(d.pop())
            else:
                Works = 'No'
                print(Works)
                break
    if Works == 'Yes':
        print(Works)
    
