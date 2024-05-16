n,m=map(int, input().split())
lst=[]
for __ in range(n-1):
    u,v,w=map(int, input().split())
    lst.append([w,u,v])
lst.sort()
ans=[0]*m
queries=sorted([[q,i] for i,q in enumerate(list(map(int, input().split())))])
a=list(range(n+1))
b=[1]*(n+1)
pntr=0
count=0

def find(x):
    while a[x]!=x:
        a[x]=a[a[x]]
        x=a[x]
    return x

for q,pos in queries:
    while pntr<n-1 and lst[pntr][0]<=q:
        w,u,v=lst[pntr]
        u,v=find(u),find(v)
        a[v]=u
        count+=b[u]*b[v]
        b[u]=b[u]+b[v]
        pntr+=1
    ans[pos]=count
print(*ans)