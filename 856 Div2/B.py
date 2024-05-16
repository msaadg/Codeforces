for __ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    for i in range((n)):
        if a[i]==1:
            a[i]+=1
    for i in range(1,n):
        if a[i]%a[i-1]==0:
            a[i]+=1
    print(*a)