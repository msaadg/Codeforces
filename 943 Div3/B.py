for __ in range(int(input())):
    n, m = map(int, input().split())
    a = input()
    b = input()
    pntr1 = 0
    pntr2 = 0

    while pntr1 < n and pntr2 < m:
        if a[pntr1] == b[pntr2]:
            pntr1 += 1
            pntr2 += 1
        else:
            pntr2 += 1

    print(pntr1)