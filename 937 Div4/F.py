import math

for __ in range(int(input())):
    a, b, c = map(int, input().split())

    height = 0
    currLevel = c

    flag = True
    while currLevel > 1:
        pcs = 0
        a1 = 0
        b1 = 0
        while a >= b and pcs < currLevel:
            a -= 1
            a1 += 1
            pcs += 2

        while a < b and pcs < currLevel:
            b -= 1
            b1 += 1
            pcs += 1

        if a < 0 or b < 0:
            print(-1)
            flag = False
            break

        currLevel = a1 + b1
        height += 1

    if flag:
        print(height + a + b)