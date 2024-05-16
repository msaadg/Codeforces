for __ in range(int(input())):
    a,b=map(int, input().split())
    n,m=map(int, input().split())
    multiplier=n//(m+1)
    rem=n-multiplier*(m+1)
    print(multiplier*min(a*m, b*(m+1))+rem*min(a,b))