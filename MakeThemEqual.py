for __ in range(int(input())):
    n, k = map(int, input().split())
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    N = 1001
    opCost = [N] * N
    opCost[1] = 0
    for i in range(1, N):
        for x in range(1, i + 1):
            j = i + i//x
            if j < N:
                opCost[j] = min(opCost[j], 1 + opCost[i])
    
    k = min(k, 12*n)
    dp = [0] * (k + 1)
    for i in range(n):
        for j in range(k, -1, -1):
            if j - opCost[b[i]] >= 0:
                dp[j] = max(dp[j], c[i] + dp[j - opCost[b[i]]])

    print(max(dp))