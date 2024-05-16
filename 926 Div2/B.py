import math
for __ in range(int(input())):
    n, k = map(int, input().split())
    if k == 4 * n - 2:
        print(k//2 + 1)
    else:
        print(math.ceil(k/2))