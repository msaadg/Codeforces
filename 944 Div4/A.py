for __ in range(int(input())):
    a = list(map(int, input().split()))
    a.sort()
    print(*a)