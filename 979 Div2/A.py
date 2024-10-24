for __ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))
  mn = min(a)
  mx = max(a)

  ans = (mx - mn) * (n - 1)

  print(ans)