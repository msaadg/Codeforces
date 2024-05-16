for __ in range(int(input())):
    n,k=map(int, input().split())
    lst=list(map(int, input().split()))
    d={}
    d1={}
    for i in range(len(lst)):
        if lst[i] not in d1:
            d[lst[i]]=i
            d1[lst[i]]=[i]
        else:
            d1[lst[i]]+=[i-d[lst[i]]-1]
            d[lst[i]]=i
    ans=10**9
    for i in d:
        d[i]=n-d[i]-1
        d1[i]+=[d[i]]
        d1[i]=sorted(d1[i], reverse=True)
        ans=min(max(d1[i][0]//2, d1[i][1]), ans)
    print(ans)