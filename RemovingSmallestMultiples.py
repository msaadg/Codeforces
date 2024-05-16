for __ in range(int(input())):
    n=int(input())
    t=input()
    lst=[0]*n
    cost=0
    for i in range(1,n+1):
        for j in range(i,n+1,i):
            if t[j-1]=='1':
                break
            if lst[j-1]==0:
                lst[j-1]=1
                cost+=i
    print(cost)