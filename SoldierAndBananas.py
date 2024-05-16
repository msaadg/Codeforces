k,n,w=map(int, input().split())
ans=sum([i for i in range(1,w+1)])*k-n
print(ans if ans>0 else 0)