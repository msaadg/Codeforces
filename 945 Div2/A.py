for __ in range(int(input())):
    a = list(map(int, input().split()))

    ans = 0
    while sum(a) != 0:
        a = sorted(a)
        if a[-1] == 0 or a[-2] == 0:
            break
            
        else:
            a[-1] -= 1
            a[-2] -= 1
            ans += 1
    
    if a[-1]%2 == 0:
        print(ans)
    else:
        print(-1)