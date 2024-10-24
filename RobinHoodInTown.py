import math

for __ in range(int(input())):
  n = int(input())
  a = sorted(list(map(int, input().split())))

  if n < 3:
    print(-1)
    continue

  mid = n//2  + 1
  w = a[mid - 1]
  if w*2 < sum(a)/n:
    print(0)
    continue
  ans = w*2 * n - sum(a)
  print(ans + 1)