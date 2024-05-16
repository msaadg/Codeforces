for __ in range(int(input())):
    n,k=map(int, input().split())
    a=list(map(int, input().split()))
    lst=[]
    for i in range(1,n):
        lst.append(abs(a[i]-a[i-1]))
    lst=sorted(lst, reverse=True)
    print(sum(lst[k-1:]))