def divisibility(n,a):
    count=0
    for i in a:
        while i%2==0:
            count+=1
            i=i/2
    req=n-count
    if req<=0:
        return 0
    else:
        lst=[]
        for x in range(1, n+1):
            count2=0
            while x%2==0:
                count2+=1
                x=x/2
            lst.append(count2)
        lst=sorted(lst, reverse=True)
        ans=0
        count3=0
        for j in lst:
            ans+=j
            count3+=1
            if ans>=req:
                return count3
        return -1

for __ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    print(divisibility(n,a))