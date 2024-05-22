import heapq

for __ in range(int(input())):
    m, x = map(int, input().split())
    c = list(map(int, input().split()))

    h = []
    cur = 0
    for i in range(m):
        if not h and c[i] > cur:
            cur += x
            continue
        elif c[i] <= cur:
            heapq.heappush(h, -c[i])
            cur -= c[i]
        elif c[i] > cur:
            mx = heapq.heappop(h)
            cur -= mx

            if c[i] > cur:
                heapq.heappush(h, mx)
                cur += mx
                cur += x
                continue
            else:
                heapq.heappush(h, -c[i])
                cur -= c[i]      

        cur += x
    
    print(len(h))