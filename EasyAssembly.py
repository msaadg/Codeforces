n=int(input())
lst,perflst=[],[]
for i in range(n):
    a=list(map(int,input().split()))
    lst.append(a[1:])
    perflst+=a[1:]
s,count=0,n
perflst=sorted(perflst)
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if j!=len(lst[i])-1 and perflst.index(lst[i][j])-perflst.index(lst[i][j+1])!=-1:
            s+=1
            count+=1

print(s,count-1)