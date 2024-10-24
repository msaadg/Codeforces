for __ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))

  m = 0
  s = 0
  ans = 0
  for i in range(n):
    m = max(m, a[i])
    s += a[i]
    if s % 2 == 0 and s // 2 == m:
      ans += 1
  print(ans)