coins = [1, 3, 6, 10, 15]
dp = [10**9 + 1] * (10**4 + 1)
dp[0] = 0

for a in range(1, 10**4 + 1):
    for c in coins:
        if a - c >= 0:
            dp[a] = min(dp[a], 1 + dp[a - c])

# write dp array to a.txt

with open('b.txt', 'w') as f:
    f.write(str(dp))
    f.close()