import heapq
for __ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    mp = {}

    for i in range(n):
        mp[a[i] >> 2] = mp.get(a[i] >> 2, []) + [a[i]]

    for i in mp:
        heapq.heapify(mp[i])

    for i in range(n):
        print(mp[a[i] >> 2][0], end = ' ')
        heapq.heappop(mp[a[i] >> 2])
    print()