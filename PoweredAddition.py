for __ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    diff=0
    val=a[0]
    for i in range(n-1):
        if a[i]>a[i+1]:
            val=max(val,a[i])
            cdiff=abs(val-a[i+1])
            diff=max(diff, cdiff)
    count=0
    while diff>0:
        diff-=2**count
        count+=1
    print(count)