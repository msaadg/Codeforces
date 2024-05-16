for __ in range(int(input())):
    s = input()
    d = {}
    lst = []
    for c in s:
        d[c] = d.get(c, 0) + 1
        lst.append(c)
    
    if len(d) == 1:
        print("NO")
    else:
        print("YES")
        lst.sort()
        if s == "".join(lst):
            lst = sorted(lst, reverse=True)
            print("".join(lst))
        else:
            print("".join(lst))