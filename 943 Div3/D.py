for __ in range(int(input())):
    n, k, pb, ps = map(int, input().split())
    p = [0] + list(map(int, input().split()))
    a = [0] + list(map(int, input().split()))

    s = set()
    b = []
    while pb not in s:
        s.add(pb)
        b.append(a[pb])
