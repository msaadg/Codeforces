for __ in range(int(input())):
    n=int(input())
    lst=list(map(int, input().split()))
    maxlst=max(lst)
    secmaxlst=sorted(lst,reverse=True)[1]
    ans=[]
    for i in lst:
        if i!=maxlst:
            ans.append(str(i-maxlst))
        else:
            ans.append(str(i-secmaxlst))
    print(' '.join(ans))