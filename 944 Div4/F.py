import math
for __ in range(int(input())):
    r = int(input())
    c = 0
    for i in range(1, r + 1):
        mini = r
        maxi = 0

        l = 0
        h = r
        while l <= h:
            mid = (l + h) // 2
            v = math.sqrt(mid**2 + i**2)
            if v >= r + 1:
                h = mid - 1 
            elif v < r + 1:
                l = mid + 1
        maxi = l - 1

        l = 0
        h = r
        while l <= h:
            mid = (l + h) // 2
            v = math.sqrt(mid**2 + i**2)
            if v >= r:
                h = mid - 1 
            elif v < r:
                l = mid + 1
        mini = h + 1

        c += (maxi - mini + 1) * 4
    
    print(c)