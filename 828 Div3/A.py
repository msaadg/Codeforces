
for __ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    s=input()
    d=dict()
    res='YES'
    for x in range(n):
        if a[x] not in d:
            d[a[x]]=s[x]
        else:
            if s[x]!=d[a[x]]:
                res='NO'
                break
    print(res)