def check(mid, a, x):
  for i in range(len(a)):
    if a[i] < mid:
      x -= mid - a[i]
  return x >= 0

for __ in range(int(input())):
  n, x = map(int, input().split())
  a = list(map(int, input().split()))

  l = 0
  r = max(a)

  ans = 1
  while l <= r:
    mid = (l + r) // 2
    if check(mid, a, x):
      ans = max(ans, mid)
      l = mid + 1
    else:
      r = mid - 1

  rem = x
  if ans == max(a):
    for i in range(n):
      rem -= ans - a[i]
    print(ans + rem//n)
  else:
    print(ans)