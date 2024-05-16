for __ in range(int(input())):
    lst = []
    for i in range(4):
        x, y = map(int, input().split())
        lst.append([x,y])
    lst.sort()

    print(abs(lst[0][0] - lst[-1][0]) * abs(lst[0][1] - lst[1][1]))