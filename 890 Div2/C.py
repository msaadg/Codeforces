for __ in range(int(input())):
    n, k = map(int, input().split())
    a = [10**9] + list(map(int, input().split()))
    for i in range(n-2, -1, -1):
        if a[i] < a[i+1] and k > 0:
            minimum = min(k, a[i+1] - a[i] + 1, a[i-1])
            a[i] += minimum
            k -= minimum
    print(max(a[1:]))