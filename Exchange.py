import math
for __ in range(int(input())):
    n,a,b=map(int, input().split())
    if a<=b:
        print(math.ceil(n/a))
    else:
        print(1)