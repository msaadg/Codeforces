for __ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))
  s = 0
  ans = 0
  last_cut = 0
  pos = {0: 0}
  for i in range(1, n + 1):
    s += a[i - 1]
    if s in pos and pos[s] >= last_cut:
      ans += 1
      last_cut = i
      pos = {}
      pos[s] = i
    else:
      pos[s] = i
  print(ans)
