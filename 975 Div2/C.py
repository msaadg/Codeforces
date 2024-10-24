for __ in range(int(input())):
  n, k = map(int, input().split())
  a = list(map(int, input().split()))

  mx, sm = max(a), sum(a)

  for i in range(n, 0, -1):
    c = (sm + k) // i
    if c >= mx and c * i > sm - 1:
      print(i)
      break