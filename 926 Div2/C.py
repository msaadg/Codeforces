import math
for __ in range(int(input())):
    k, x, a = map(int, input().split())
    needed = math.ceil((x - 1) / k)
    a -= (x - 1)
    if needed  > a:
        print('yes')
    else:
        print('no')