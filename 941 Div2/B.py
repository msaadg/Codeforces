for __ in range(int(input())):
    n, m = map(int, input().split())
    rows, cols = [], [[] for _ in range(m)]
    for i in range(n):
        lst = list(input())
        rows.append(lst)
        for j in range(m):
            cols[j].append(lst[j])
    
    if rows[0][0] == rows[n - 1][m - 1]:
        print("YES")
    elif rows[0][m - 1] == rows[n - 1][0]:
        print("YES")
    else:
        if rows[0][0] == rows[n - 1][0] and rows[0][0] in cols[m - 1]:
            print("YES")
        elif rows[0][0] == rows[0][m - 1] and rows[0][0] in rows[n - 1]:
            print("YES")
        elif rows[n - 1][0] == rows[n - 1][m - 1] and rows[n - 1][0] in rows[0]:
            print("YES")
        elif rows[n - 1][m - 1] == rows[0][m - 1] and rows[0][m - 1] in cols[0]:
            print("YES")
        else:
            print("NO")