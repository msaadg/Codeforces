for __ in range(int(input())):
    a,b,c=sorted(map(int, input().split()))
    ans=0
    if a>0:
        ans+=1
        a-=1
    if b>0:
        ans+=1
        b-=1
    if c>0:
        ans+=1
        c-=1
    if c>0 and a>0:
        ans+=1
        c-=1
        a-=1
    if c>0 and b>0:
        ans+=1
        c-=1
        b-=1
    if a>0 and b>0:
        ans+=1
        a-=1
        b-=1
    if c>0 and b>0 and a>0:
        ans+=1
    print(ans)