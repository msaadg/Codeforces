for __ in range(int(input())):
    k,n=map(int, input().split())
    i=1
    gap=0
    count=n-k+1
    lst=[]
    while i<=n and i<=count and gap+1<=k:
        lst.append(i)
        gap+=1
        i+=gap
        count+=1
    while count<n+1:
        lst.append(lst[-1]+1)
        count+=1
    for i in lst:
        print(i,end=' ')
    print()