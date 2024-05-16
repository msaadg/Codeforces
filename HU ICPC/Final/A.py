n,k=map(int, input().split())
lst=list(map(int, input().split()))
d1,d2={},{}
ans=0
for a in lst:
    if a%k==0:
        ans+=d1.get(a/k,0)
        d1[a]=d1.get(a,0)+d2.get(a/k,0)
    d2[a]=d2.get(a,0)+1
print(ans)