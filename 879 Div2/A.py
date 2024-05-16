import math
for __ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    count1=0
    count2=1
    ans=0
    for i in a:
        count1+=i
        count2*=i
    if count1<0:
        count1=math.ceil(-count1/2)
        count2=count2*((-1)**count1)
        ans=count1
    if count2<0:
        print(ans+1)
    else:
        print(ans)