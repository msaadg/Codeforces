for __ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))

  x = b[-1]
  mn = 10**10
  ans = 0

  for i in range(n):
    if abs(a[i] - x) < mn:
      mn = abs(a[i] - x)
    
    if abs(b[i] - x) < mn:
      mn = abs(b[i] - x)

    if a[i] <= x <= b[i] or b[i] <= x <= a[i]:
      mn = 0
  
    ans += abs(b[i] - a[i])
  
  ans += mn
  print(ans + 1)
  