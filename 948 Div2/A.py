for __ in range(int(input())):
    n, m = map(int, input().split())
    cur = 0
    for i in range(n):
        if cur < m:
            cur += 1
        else:
            cur -= 1
    print("Yes" if cur == m else "No")