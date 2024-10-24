for __ in range(int(input())):
  n = int(input())
  d = {}
  for i in range(n):
    row = list(map(int, input().split()))
    # print(row)
    for j in range(n):
      if i - j not in d and row[j] < 0:
        d[i - j] = abs(row[j])
      elif i - j in d and row[j] < 0:
        d[i - j] = max(d[i - j], abs(row[j]))
  
  print(sum(d.values()))