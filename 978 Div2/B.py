import math

for __ in range(int(input())):
  n, x = map(int, input().split())
  a = list(map(int, input().split()))

  sm = sum(a)
  mx = max(a)

  print(max(mx, math.ceil(sm / x)))