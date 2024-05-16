from bisect import bisect_left as bl
for __ in range(int(input())):
    n, k, q = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    b = [0] + list(map(int, input().split()))

    ans = []
    for _ in range(q):
        d = int(input())
        l = bl(a, d)
        ans.append((d - a[l - 1])*(b[l] - b[l - 1])//(a[l] - a[l - 1]) + b[l - 1])
    
    print(*ans)