from bisect import bisect_left
for __ in range(int(input())):
  n, q = map(int, input().split())
  x = list(map(int, input().split()))
  k = list(map(int, input().split()))

  sumArray = [0] * (n)
  sumArray[0] = n - 1
  for i in range(1, n):
    sumArray[i] = sumArray[i-1] + n - i - 1

  d = {}
  for i in range(n):
    index = bisect_left(x, x[i])
    key = int(sumArray[index] - ((index*(index - 1))/2))
    d[key] = d.get(key, 0) + 1

    if i > 0 and x[i] - x[i-1] > 1:  
      index = bisect_left(x, x[i] - 1)
      key = int(sumArray[index - 1] - ((index*(index - 1))/2))
      d[key] = d.get(key, 0) + (x[index] - x[index - 1] - 1)
  

  for i in range(q):
    if k[i] in d:
      print(d[k[i]], end = " ")
    else:
      print(0, end = " ")
  print()