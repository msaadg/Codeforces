for __ in range(int(input())):
    n, k = map(int, input().split())
    c = sorted(list(map(int, input().split())))

    same = 1
    maxs = 0
    for i in range(1, n):
        if c[i] == c[i - 1]:
            same += 1
            maxs = max(maxs, same)

        else:
            same = 1

    if maxs >= k:
        print(k - 1)
    else:
        print(n)