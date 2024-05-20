for __ in range(int(input())):
    x, y = map(int, input().split())

    ans = 0
    while x > 0 or y > 0:
        ans += 1
        if y >= 2:
            y -= 2
            x -= 7
        elif y == 1:
            y -= 1
            x -= 11
        else:
            x -= 15
    print(ans)