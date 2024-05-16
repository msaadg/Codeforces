for __ in range(int(input())):
    n, m = map(int, input().split())
    d1, lst = {}, []
    flag = True
    for i in range(m):
        a, b, d = map(int, input().split())
        lst.append((a, b, d))
    for a, b, d in lst:
        if a not in d1 and b not in d1:
            d1[a] = 0
            d1[b] = d1[a] + d
        elif a not in d1 and b in d1:
            d1[a] = d1[b] - d
        elif b not in d1 and a in d1:
            d1[b] = d1[a] + d
        elif a in d1 and b in d1:
            if d1[a] + d != d1[b]:
                print("NO")
                flag = False
                break
    if flag: print("YES")