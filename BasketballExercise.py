n = int(input())
h1 = list(map(int, input().split()))
h2 = list(map(int, input().split()))

dp1 = [0] * (n + 1)
dp2 = [0] * (n + 1)

for i in range(1, n + 1):
    dp1[i] = max(dp1[i - 1], h1[i - 1] + dp2[i - 1])
    dp2[i] = max(dp2[i - 1], h2[i - 1] + dp1[i - 1])

print(max(dp1[n], dp2[n]))