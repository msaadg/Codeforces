from bisect import bisect_left as bl
for __ in range(int(input())):
    x = int(input())
    dp = [0] * 32
    dp[0] = 1
    dp[1] = 2

    for i in range(2, 32):
        dp[i] = dp[i - 2] + 2**i
    
    n = bl(dp, x)
    ans = [0] * (n + 1)
    ans[n] = 1
    cur = 2**n
    while cur != x:
        idx = bl(dp, abs(x - cur))
        if cur > x:
            ans[idx] = -1
            cur -= 2**idx
        else:
            ans[idx] = 1
            cur += 2**idx
    print(n + 1)
    print(*ans)