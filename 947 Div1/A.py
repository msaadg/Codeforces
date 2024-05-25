for __ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a1 = sorted(a.copy())

    pntr1, pntr2 = 1, n - 2

    while pntr1 < n and a[pntr1 - 1] <= a[pntr1]:
        pntr1 += 1
    
    while pntr2 > -1 and a[pntr2 + 1] >= a[pntr2]:
        pntr2 -= 1

    if a[pntr2 + 1:] + a[:pntr1] == a1 or a == a1:
        print('Yes')
    else:
        print('No')