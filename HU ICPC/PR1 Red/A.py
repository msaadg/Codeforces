for __ in range(int(input())):
    n,m=map(int, input().split())
    lst=[]
    ans=10**9
    for _ in range(n):
        lst.append(input())
    for i in range(n):
        for j in range(i+1,n):
            count=0
            for k in range(m):
                count+=abs(ord(lst[i][k])-ord(lst[j][k]))
            ans=min(ans, count)
    print(ans)