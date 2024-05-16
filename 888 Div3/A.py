for __ in range(int(input())):
    n,m,k,H=map(int,input().split())
    h=list(map(int,input().split()))
    count=0
    for i in range(n):
        if abs(h[i]-H)%k==0 and abs(h[i]-H)/k<=(m-1) and h[i]!=H:
            count+=1
    print(count)