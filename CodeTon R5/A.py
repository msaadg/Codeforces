for __ in range(int(input())):
    n,m=map(int, input().split())
    lst1=list(map(int, input().split()))
    lst2=list(map(int, input().split()))
    sum1=sum(lst1)
    sum2=sum(lst2)
    if sum1>sum2:
        print("Tsondu")
    elif sum2>sum1:
        print("Tenzing")
    else:
        print("Draw")