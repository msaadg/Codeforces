def route(parent,i,m,cc,cats,a):
    cc=cats[parent]+a[i] if a[i] else 0
    cats[i]=cc
    if len(d[i])==1 and d[i][0]==parent and cc<=m:
        return 1
    elif cc>m:
        return 0
    elif cc<=m and i in d:
        rfinal=0
        for j in d[i]:
            if j!=parent:
                rfinal+=route(i,j,m,cc,cats,a)
        return rfinal

import sys
u=sys.stdin.readline
n,m=map(int, u().split())
a=[0]+list(map(int, u().split()))
d={}
cats={1:a[1]}
for __ in range(n-1):
    x,y=map(int, input().split())
    d[x]=d.get(x,[])+[y]
    d[y]=d.get(y,[])+[x]
cc=a[1]
parent=1
final=0
for i in d[1]:
    final+=route(parent,i,m,cc,cats,a)
print(final)