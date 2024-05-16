for __ in range(int(input())):
    n=int(input())
    a=sorted(map(int, input().split()))
    if n==1:
        print(0)
    else:
        ans=0
        for i in range(n//2):
            ans+=a[n-1-i]-a[i]
        print(ans)