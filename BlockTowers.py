import math
for __ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    lst,t1=[],a[0]
    for i in sorted(a[1:]):
        if i>t1:
            t1+=math.ceil((i-t1)/2)
    print(t1)