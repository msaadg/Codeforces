n=int(input())
p=list(map(int, input().split()))
i=n-2
lst=[1,n]
while p[i]!=1:
    lst.append(p[i])
    i=p[i]-2
print(*sorted(lst))