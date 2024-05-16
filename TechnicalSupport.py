for __ in range(int(input())):
    n=int(input())
    s=input()
    count=0
    for i in s:
        if i=='Q':
            count+=1
        else:
            count-=1
            if count==-1:
                count=0
    if count>0:
        print('NO')
    else:
        print('YES')