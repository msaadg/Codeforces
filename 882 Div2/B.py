for __ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    if n==1:
        print(1)
    else:
        curr=a[0]
        for i in range(1,n):
            curr=curr&a[i]

        ans=0
        newcurr=a[0]
        for i in range(n):
            newcurr=newcurr&a[i]
            if newcurr==curr:
                ans+=1
                if i==(n-1):
                    break
                else:
                    newcurr=a[i+1]
        print(ans)