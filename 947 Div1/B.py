for __ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))

    x, y = a[0], a[1]

    count = 2
    while y % x == 0 and count < n:
        y = a[count]
        count += 1

    flag = True
    for i in range(n):
        if a[i] % x == 0 or a[i] % y == 0:
            continue
        else:
            flag = False
            break
    
    if flag:
        print("Yes")
    else:
        print("No")