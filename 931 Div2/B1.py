for __ in range(int(input())):
    n = int(input())
    coins = [1, 3, 6, 10, 15]
    dp = [10**9 + 1] * (n + 1)
    dp[0] = 0

    for c in coins:
        for a in range(1, n + 1):
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])

    print(dp[n])