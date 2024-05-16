for __ in range(int(input())):
    n,x=map(int, input().split())
    stk1=list(map(int, input().split()))
    stk2=list(map(int, input().split()))
    stk3=list(map(int, input().split()))
    c1=0
    c2=0
    c3=0
    k=0
    flag=False
    while k<=x:
        if k==x:
            flag=True
            break
        lst=[]
        if c1<n:
            lst.append((stk1[c1],"c1"))
        if c2<n:
            lst.append((stk2[c2],"c2"))
        if c3<n:
            lst.append((stk3[c3],"c3"))
        if len(lst)>0:
            mini=min(lst)
            k=k|mini[0]
            if mini[1]=="c1":
                c1+=1
            elif mini[1]=="c2":
                c2+=1
            else:
                c3+=1
        else:
            break
    if flag==True:
        print('Yes')
    else:
        print('No')