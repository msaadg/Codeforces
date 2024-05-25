for __ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    m = a[(0 + n) // 2 - 1]
    for i in range(1, n):
        x, y = a[i - 1], a[i]
        if x > y:
            x, y = y, x
        m = max(m, x)
    
    print(m)