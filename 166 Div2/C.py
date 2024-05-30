for __ in range(int(input())):
  n, m = map(int, input().split())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))

  nC, mC = n, m
  pbp, tbp = n + m, n + m

  ans = [0] * (n + m)
  for i in range(n + m + 1):
    if a[i] > b[i] and nC > 0:
      nC -= 1
      continue
    elif b[i] > a[i] and mC > 0:
      mC -= 1
      continue
    
    if pbp == n + m and (a[i] > b[i] and nC == 0 or mC == 0):
      pbp = i
    if tbp == n + m and (b[i] > a[i] and mC == 0 or nC == 0):
      tbp = i
  
  c = 0
  nC, mC = n, m
  ans = [0] * (n + m + 1)
  arr = [""] * (n + m + 1)
  for i in range(n + m + 1):
    if a[i] > b[i]:
      if nC > 0:
        c += a[i]
        nC -= 1
        arr[i] = "p"
      else:
        c += b[i]
        mC -= 1
        arr[i] = "t"
    else:
      if mC > 0:
        c += b[i]
        mC -= 1
        arr[i] = "p"
      else:
        c += a[i]
        nC -= 1
        arr[i] = "t"

  ans[n + m] = c