for __ in range(int(input())):
    n=int(input())
    l=sorted(list(map(int, input().split())))
    count=0
    prevcount=101
    flag=True
    for i in range(n):
        if i==0 and l[i]!=0:
            flag=False
            break
        if i!=0 and l[i]!=l[i-1]:
            if count>prevcount or l[i]-l[i-1]>1:
                flag=False
                break
            prevcount=count
            count=1
        else:
            count+=1
    if count>prevcount:
        flag=False
    print("Yes" if flag==True else 'No')

