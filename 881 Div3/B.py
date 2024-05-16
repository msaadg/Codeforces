for __ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    flag=True
    count=0
    for i in range(n):
        if a[i]>0:
            flag=True
        elif a[i]<0:
            a[i]=-a[i]
            if flag==True:
                count+=1
            flag=False
    print(sum(a), count)