for __ in range(int(input())):
    n = int(input())
    s = list(input())

    s1 = sorted(s)
    s2 = set()
    lst = []
    for i in range(n):
        if s1[i] not in s2:
            s2.add(s1[i])
            lst.append(s1[i])
    
    pntr1 = 0
    pntr2 = len(lst) - 1

    mp = {}
    while pntr1 < pntr2:
        mp[lst[pntr1]] = lst[pntr2]
        mp[lst[pntr2]] = lst[pntr1]

        pntr1 += 1
        pntr2 -= 1
    
    for i in range(n):
        if s[i] not in mp:
            print(s[i], end = "")
        else:
            print(mp[s[i]], end = "")
    print()
