for __ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))

  ans = []
  for i in range(1, n):
    if a[i] < a[i-1]:
      ans.append(a[i - 1] - a[i])
      a[i] = a[i - 1]
  
  print(sum(ans) + max(ans) if ans else 0)