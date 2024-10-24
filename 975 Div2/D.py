from collections import deque

for __ in range(int(input())):
  n = int(input())
  a = deque([(int(s), i) for i, s in enumerate(input().split())])

  l, r = 0, n - 1

  for i in range(n, 0, -1):
    if len(a) > i:
      print(0)
      break
    
    l = max(l, a[-1][1] - i + 1)
    r = min(r, a[0][1] + i - 1)
    
    while a and a[0][0] >= i:
      a.popleft()
    while a and a[-1][0] >= i:
      a.pop()
    if not a:
      print(r - l + 1)
      break