import math
n,k=map(int, input().split())
if n<k:
    print('NO')
else:
    d={}
    count=0
    while n>0:
        x=int(math.log2(n))
        n-=2**x
        d[x]=1
        count+=1
    # print(d)
    # print(count)
    if count<=k:
        while count<k:
            for key,value in sorted(d.items(),reverse=True):
                if value>0:
                    d[key-1]=d.get(key-1,0)+2
                    d[key]=d.get(key)-1
                    count+=1
                    break
        print('YES')
        for key,value in d.items():
            for i in range(value):
                print(2**key, end=' ')
    else:
        print('NO')