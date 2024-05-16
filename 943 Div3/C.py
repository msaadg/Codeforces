for __ in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))

    m = max(x) + 1
    a = [0] * n

    a[0] = m
    for i in range(1, n):
        a[i] = m + x[i - 1]
        m = a[i]
    
    print(*a)