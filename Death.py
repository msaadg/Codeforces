for __ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    b=sorted(list(map(int, input().split())))
    print(sum(a)+sum(b[:n-1]))