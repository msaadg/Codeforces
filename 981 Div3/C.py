t = int(input())
for _ in range(t):
  n = int(input())
  a = list(map(int, input().split()))

  for i in range(1, n//2):
    if a[i] == a[i - 1] or a[n - i - 1] == a[n - i]:
      temp = a[i]
      a[i] = a[n - i - 1]
      a[n - i - 1] = temp
  
  ans = 0
  for i in range(1, n):
    if a[i] == a[i - 1]:
      ans += 1
  print(ans)