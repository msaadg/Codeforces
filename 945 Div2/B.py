for __ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    lst = [0] * n
    lst[0] = a[0]

    for i in range(1, n):
        lst[i] = a[i] | lst[i - 1]
    
    iprev, jprev, i, j = 0, n - 1, 0, n - 2

    flag = True
    ans = 0
    while i < j and iprev < jprev:
        if lst[i] == lst[iprev] and lst[j] == lst[jprev]:
            ans = min(ans, i - j)

        if flag:
            iprev = i
            i -= 1
            flag = False
        else:
            jprev = j
            j -= 1
            flag = True
    
    print(j - i + 1)