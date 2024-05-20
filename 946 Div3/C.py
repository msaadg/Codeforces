for __ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    mp = {}
    ans = 0 
    for i in range(n - 2):
        x, y, z = a[i], a[i + 1], a[i + 2]
        if (x, y, 0) in mp:
            ans += mp[(x, y, 0)]
        if (0, y, z) in mp:
            ans += mp[(0, y, z)]
        if (x, 0, z) in mp:
            ans += mp[(x, 0, z)]

        if (x, y, z) in mp:
            ans -= 3 * mp[(x, y, z)]
        
        mp[(x, y, 0)] = mp.get((x, y, 0), 0) + 1
        mp[(0, y, z)] = mp.get((0, y, z), 0) + 1
        mp[(x, 0, z)] = mp.get((x, 0, z), 0) + 1
        mp[(x, y, z)] = mp.get((x, y, z), 0) + 1
    print(ans)