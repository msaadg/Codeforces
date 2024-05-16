for __ in range(int(input())):
    s=input()
    m=int(input())
    l=input()
    r=input()
    d,d1={},{}
    flag=False
    for i in range(len(s)):
        d[int(s[i])]=d.get(int(s[i]),[])+[i]
    for i in range(m):
        for j in range(int(l[i]), int(r[i])+1):
            if tuple(d[j]) in d1 and len(d[j])<(i+1):
                flag=True
            elif i==m-1 and j not in d:
                flag=True
            d1[tuple(d[j])]=d.get(tuple(d[j]),0)+1
    if flag==False:
        print("No")
    else:
        print("Yes")