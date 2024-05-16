for __ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    mini=10**9
    flag=True
    for i in range(n-1):
        if a[i]>a[i+1]:
            flag=False
            break
        else:
            mini=min(a[i+1]-a[i], mini)
    if flag:
        print((mini//2)+1)
    else:
        print(0)