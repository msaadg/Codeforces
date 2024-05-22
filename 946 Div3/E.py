for __ in range(int(input())):
    m, x = map(int, input().split())
    c, h = [], []
    for i in range(m):
        ci, hi = map(int, input().split())
        c.append(ci)
        h.append(hi)

    maxh = sum(h)
    dp = [float('inf')] * (maxh + 1)
    dp[0] = 0

    for i in range(m):
        ci = c[i]
        hi = h[i]
        for j in range(maxh, -1, -1):
            if j - hi >= 0 and ci + dp[j - hi] <= i * x:
                dp[j] = min(dp[j], ci + dp[j - hi])
    
    for i in range(maxh, -1, -1):
        if dp[i] != float('inf'):
            print(i)
            break