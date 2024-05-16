n,m=map(int,input().split())
count=0
while m>n:
    if m%2==0:
        m=int(m/2)
        count+=1
    else:
        m+=1
        count+=1
print(count+n-m)