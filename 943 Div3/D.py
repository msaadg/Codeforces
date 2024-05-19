for __ in range(int(input())):
    n, k, pb, ps = map(int, input().split())
    p = [0] + list(map(int, input().split()))
    a = [0] + list(map(int, input().split()))

    b, bcurr = 0, 0
    s, scurr  = 0, 0
    for i in range(min(n, k)):
        b = max(b, bcurr + (k - i) * a[pb])
        s = max(s, scurr + (k - i) * a[ps])

        bcurr += a[pb]
        scurr += a[ps]

        pb = p[pb]
        ps = p[ps]

    if b > s:
        print("Bodya")
    elif s > b:
        print("Sasha")
    else:
        print("Draw")