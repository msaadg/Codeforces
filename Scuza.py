import bisect
for __ in range(int(input())):
    n,q=map(int, input().split())
    a=list(map(int, input().split()))
    k=list(map(int, input().split()))
    maxlst,sumlst=[],[0]
    m=0
    for i in a:
        m=max(m,i)
        maxlst.append(m)
        sumlst.append(sumlst[-1]+i)
    for i in k:
        pos=bisect.bisect(maxlst,i)
        print(sumlst[pos],end=' ')
    print()