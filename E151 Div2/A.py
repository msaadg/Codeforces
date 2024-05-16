for __ in range(int(input())):
    n,k,x=map(int, input().split())
    flag=False
    for i in range(1,k+1):
        if i!=x and n%i<=k and n%i!=x:
            print("Yes")
            print(n//i if n%i==0 else n//i+1)
            print((str(i)+" ")*(n//i), end="")
            if n%i!=0:
                print(str(n%i), end="")
            flag=True
            print()
            break
    if flag==False:
        print("No")