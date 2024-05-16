for __ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    maxc = 0
    count = 1
    for i in range(1, n):
        if a[i] - a[i-1] <= k:
            count += 1
        else:
            maxc = max(maxc, count)
            count = 1
    maxc = max(maxc, count)
    print(n - maxc)