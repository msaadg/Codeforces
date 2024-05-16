for __ in range(int(input())):
    n,q=map(int, input().split())
    a=list(map(int, input().split()))
    q1=0
    ans=''
    for i in range(n-1,-1,-1):
        if q1<a[i]:
            if q1<q:
                q1+=1
                ans+='1'
            else:
                ans+='0'
        else:
            ans+='1'
    print(ans[::-1])