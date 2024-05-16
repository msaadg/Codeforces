lst,antidiag=[],[]
n=int(input())
for i in range(n):
    a=list(map(int, input().split()))
    antidiag.append(a[n-1-i])
    lst.append(a)
mindiag=min(antidiag)
ans=0
for i in lst:
    ans+=sum(i)
print(ans-mindiag)