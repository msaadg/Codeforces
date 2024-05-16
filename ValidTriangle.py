for __ in range(int(input())):
    a,b,c=map(int, input().split())
    print('Yes' if a+b>c and a+c>b and b+c>a else 'No')