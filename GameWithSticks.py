n,m = map(int, input().split())
prod=n*m
count=0
while prod>0:
    n=n-1
    m=m-1
    prod=n*m
    count+=1
if count%2==1:
    print('Akshat')
else:
    print('Malvika')