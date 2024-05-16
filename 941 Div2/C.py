for __ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))

    s = set()
    lst = []
    for i in range(n):
        if a[i] in s:
            continue
        else:
            s.add(a[i])
            lst.append(a[i])

    turn = True     # Alice  
    ans = []
    count = 0
    for i in range(len(lst)):
        if lst[i] - count == 1:
            if i != 0:
                ans.append(turn)
            else:
                ans.append(turn)
                turn = not turn
            
        else:
            ans.append(turn)
        # last = lst[i] - count
        count += lst[i] - count

    print("Alice" if ans[-1] else "Bob")