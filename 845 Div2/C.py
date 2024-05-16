factors=[[] for i in range(10**5+1)]
for i in range(1,10**5+1):
    for j in range(i, 10**5+1, i):
        factors[j].append(i)
for __ in range(int(input())):
    n,m=map(int, input().split())
    a=sorted(list(map(int, input().split())))
    maxa=a[-1]
    ans=a[-1]-a[0]+1
    c=[0 for i in range(m+1)]
    counter=0
    j=0
    for i in range(n):
        while j<n and counter<m:
            for x in factors[a[j]]:
                if x<=m:
                    c[x]+=1
                    if c[x]==1:
                        counter+=1
            j+=1
        if counter==m:
            ans=min(ans,a[j-1]-a[i])
        for x in factors[a[i]]:
            if x<=m:
                c[x]-=1
                if c[x]==0:
                    counter-=1
    if ans==a[-1]-a[0]+1:
        print(-1)
    else:
        print(ans)