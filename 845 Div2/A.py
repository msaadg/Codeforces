for __ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    count=0
    for i in range(len(a)-1):
        if a[i]%2==0 and a[i+1]%2==0:
            count+=1
        elif a[i]%2==1 and a[i+1]%2==1:
            count+=1
    print(count)