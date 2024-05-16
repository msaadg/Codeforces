for _ in range(int(input())):
    n,m,k=map(int, input().split())
    vx,vy=map(int, input().split())
    lst=[]
    for i in range(k):
        x,y=map(int, input().split())
        lst.append((x,y))
    if k==1:
        print('Yes')
    else:
        flag=True
        for x,y in lst:
            if abs(x-vx)+abs(y-vy)==1:
                print('Yes')
                flag=False
                break
        if flag:
            print('No')