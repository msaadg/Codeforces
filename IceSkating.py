def drift(visited,dx,dy,x,y):
    for a in dx[x]:
        if (x,a) not in visited and a!=y:
            visited.append((x,a))
            drift(visited,dx,dy,x,a)
    for b in dy[y]:
        if (b,y) not in visited and b!=x:
            visited.append((b,y))
            drift(visited,dx,dy,b,y)
    return

n=int(input())
visited=[]
dx={}
dy={}
lenprevious,total=0,0
for __ in range(n):
    x,y=map(int, input().split())
    dx[x]=dx.get(x,[])+[y]
    dy[y]=dy.get(y,[])+[x]
for x in dx:
    for y in dx[x]:
        if (x,y) not in visited:
            visited.append((x,y))
            drift(visited,dx,dy,x,y)
            connected=len(visited)-lenprevious-1
            lenprevious=len(visited)
            total+=connected
print(n-total-1)