lst=list(map(int, input().split()))
if lst.count(0)==1 and lst.count(1)==1:
    print(1)
elif lst.count(0)==1 and lst.count(1)==2:
    print(0)
elif lst.count(0)==2:
    print(0)
else:
    if lst[0]>=lst[1]*2+lst[2]*2 or lst[1]>=lst[0]*2+lst[2]*2 or lst[2]>=lst[0]*2+lst[1]*2:
        maxl=max(lst)
        x=0
        for i in lst:
            if i!=maxl:
                x+=i
        print(x)
    else:
        print(sum(lst)//3)