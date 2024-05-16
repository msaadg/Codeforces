import math
for __ in range(int(input())):
    x = int(input())
    ans = 1
    for y in range(1, x):
        if math.gcd(x, y) + y > math.gcd(x, ans) + ans:
            ans = y
    print(ans)