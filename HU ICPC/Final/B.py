n,m=map(int, input().split())
matrix=[]
for __ in range(n):
    matrix.append(list(map(int, input().split())))
flag=True
for j in range(m-1, -1, -1):
    i=n-1
    j2=j
    while i>=0 and j2<m:
        if matrix[i][j2]==0:
            matrix[i][j2]=min(matrix[i+1][j2]-1,matrix[i][j2+1]-1)
        elif i<n-1 and matrix[i][j2]>=matrix[i+1][j2]:
                flag=False
        elif j2<m-1 and matrix[i][j2]>=matrix[i][j2+1]:
                flag=False
        i-=1
        j2+=1

for i in range(n-1, -1, -1):
    i2=i
    j=0
    while i2>=0 and j<m:
        if matrix[i2][j]==0:
            matrix[i2][j]=min(matrix[i2+1][j]-1,matrix[i2][j+1]-1)
        elif i2<n-1 and matrix[i2][j]>=matrix[i2+1][j]:
                flag=False
        elif j<m-1 and matrix[i2][j]>=matrix[i2][j+1]:
                flag=False
        i2-=1
        j+=1

count=0
if flag==True:
    for i in matrix:
        count+=sum(i)
    print(count)
else:
    print(-1)