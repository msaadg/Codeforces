import math
for __ in range(int(input())):
    n=int(input())
    print(n*(n-1)*math.factorial(n)%(10**9+7))