def solve(c, h, x, dp, currh, currx, i):
    if i == len(c):
        return currh
    if dp[i] != -1:
        return dp[i]
    
    val1, val2 = 0, 0
    if currx >= c[i]:
        val1 = solve(c, h, x, dp, currh + h[i], currx - c[i] + x, i + 1)
    val2 = solve(c, h, x, dp, currh, currx + x, i + 1)
    dp[i] = max(val1, val2)
    return dp[i]

for __ in range(int(input())):
    m, x = map(int, input().split())
    c, h = [], []
    for i in range(m):
        a, b = map(int, input().split())
        c.append(a)
        h.append(b)

    dp = [-1] * m
    solve(c, h, x, dp, 0, 0, 0)

    print(dp[0])