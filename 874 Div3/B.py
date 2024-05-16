for __ in range(int(input())):
    n,k=map(int, input().split())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    c=sorted([[v,i] for i,v in enumerate(a)])
    b=sorted(b)
    ans=[0]*n
    for i in range(n):
        ans[c[i][1]]=b[i]
    print(*ans)