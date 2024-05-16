for __ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    copya=sorted(a)
    flag=True
    for i in range(n):
        if a[i]%2==0 and copya[i]%2==1:
            flag=False
            print("NO")
            break
    if flag:
        print("YES")