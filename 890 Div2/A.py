for __ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    asort = sorted(a)
    flag = True
    for i in range(n-1, -1, -1):
        if asort[i]!=a[i]:
            print(asort[i])
            flag=False
            break
    if flag:
        print(0)
    