for __ in range(int(input())):
    n, f, a, b = map(int, input().split())
    lst = list(map(int, input().split()))
    # lst.append(0)

    totalcost = 0
    curr = 0
    for i in range(n):
        travel = (lst[i] - curr) * a
        jump = b

        cost = min(travel, jump)

        totalcost += cost
        curr = lst[i]

    if totalcost < f:
        print("YES")
    else:
        print("NO")