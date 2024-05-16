from math import isqrt
t = int(input())
for i in range (t):
    n = int(input())
    ans = (1 + isqrt(1 + 8*n))//2
    ans1 = (ans*(ans - 1))//2
    d = n - ans1
    print(d + ans)