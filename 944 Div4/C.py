for __ in range(int(input())):
    a, b, c, d = map(int, input().split())
    a, b = sorted([a, b])

    one = 0
    two = 0
    for i in range(a, b + 1):
        if i == c or i == d:
            one += 1
    
    a, b = b, a
    for i in range(a, b + 12 + 1):
        if i == c or i == d or i - 12 == c or i - 12 == d:
            two += 1
    
    if one == 2 or two == 2:
        print("NO")
    else:
        print("YES")