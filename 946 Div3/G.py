import heapq
for __ in range(int(input())):
    m, x = map(int, input().split())
    c = list(map(int, input().split()))

    h = []
    cur = 0

    for i in range(m):
        if c[i] <= cur:
            heapq.heappush(h, -c[i])
            cur -= c[i]
        elif h and -h[0] > c[i]:
            cur += -heapq.heappop(h) - c[i]
            heapq.heappush(h, -c[i])
        cur += x
    
    print(len(h))