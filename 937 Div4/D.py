def check(n):
    while n > 0:
        if n % 10 != 0 and n % 10 != 1:
            return False
        n //= 10

    return True

dp = [0] * (10**5 + 1)

dp[0] = 1
dp[1] = 1

for i in range(2, 10**5 + 1):
    if check(i):
        dp[i] = 1

    else:
        for mplier in range(1, int(i**0.5) + 1):
            mcand = i // mplier
            if i % mplier == 0 and dp[mplier] == 1 and dp[mcand] == 1:
                dp[i] = 1

for __ in range(int(input())):
    n = int(input())
    if dp[n] == 1:
        print("YES")
    else:
        print("NO")