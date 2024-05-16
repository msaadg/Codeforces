for __ in range(int(input())):
    n,k=map(int, input().split())
    need=(k-1)//(n-1)
    print(k+need)