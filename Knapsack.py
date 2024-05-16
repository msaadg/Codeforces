import math

for __ in range(int(input())):
    n, W = map(int, input().split())
    w = list(map(int, input().split()))

    s = 0
    lst = []
    flag = False
    for i in range(n):
        if w[i] >= math.ceil(W/2) and w[i] <= W:
            print(1)
            print(i + 1)
            flag = True
            break
        
        elif w[i] > W:
            continue
            
        else:
            s += w[i]
            lst.append(i + 1)
        
        if s >= math.ceil(W/2) and s <= W:
            print(len(lst))
            print(*lst)
            flag = True
            break
    
    if not flag:
        print(-1)