def check(mid, lst):
    count=0
    for i in lst:
        if i[0]>=mid-count-1 and i[1]>=count:
            count+=1
            if count==mid:
                return True
    return False
 
def binary_search(n,lst):
    l,r=1,n
    ans=0
    while l<=r:
        mid=l+(r-l)//2
        if check(mid, lst) == True:
            ans=mid
            l=mid+1
        else:
            r=mid-1
    return ans

import sys
u=sys.stdin.readline
for __ in range(int(u())):
    n=int(u())
    lst=[]
    for i in range(n):
        lst.append(list(map(int, u().split())))
    print(binary_search(n,lst))