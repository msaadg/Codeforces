for __ in range(int(input())):
    L,R=input().split()
    l,r=len(L),len(R)
    length=max(l,r)
    lst=[0]*length
    if l<r:
        L='0'*(r-l)+L
    elif r<l:
        R='0'*(l-r)+R
    for i in range(length):
        if i!=0 and lst[i-1]>=1:
            lst[i]=9
        else:
            lst[i]=abs(int(L[i])-int(R[i]))
    print(sum(lst))