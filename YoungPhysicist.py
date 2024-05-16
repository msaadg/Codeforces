x,y,z=0,0,0
for __ in range(int(input())):
    i,j,k=map(int, input().split())
    x+=i
    y+=j
    z+=k
print('YES' if x==y==z==0 else 'NO')