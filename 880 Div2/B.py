import math
for __ in range(int(input())):
    n,k,g=map(int, input().split())
    limit=math.ceil(g/2)-1
    total=k*g
    if g==2:
        print(0)
        continue
    ans=limit*(min(total//limit, n-1))
    total-=limit*(min(total//limit, n-1))
    if total>0:
        r=total%g
        if (total%g)>=math.ceil(g/2):
            ans+=total-(total+(g-r))
        else:
            ans+=total-(total-r)
    print(ans)