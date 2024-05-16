d=int(input())
n=int(input())
months=list(map(int, input().split()))
ans=0
for x in range(len(months)-1):
    ans+=d-months[x]
print(ans)