import sys
t = int(sys.stdin.readline())
for _ in range(t):
  n = int(sys.stdin.readline())
  p = list(map(int, sys.stdin.readline().split()))
  swaps = 0
  for i in range(n):
    if p[i] > 0:
      current = i
      length = 0
      while p[current] > 0:
        temp = p[current] - 1
        p[current] = -p[current]
        current = temp
        length += 1
      if length >= 3:
        swaps += (length - 1) // 2
  print(swaps)