for __ in range(int(input())):
    n=int(input())
    a=input()
    count,ans=int(a[0]),''
    for i in range(1,n):
        if count>0:
            ans+='-'
            count-=int(a[i])
        else:
            ans+='+'
            count+=int(a[i])
    print(ans)