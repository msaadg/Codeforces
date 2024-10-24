for __ in range(int(input())):
  n = int(input())
  lst = []
  for i in range(n):
    lst.append(list(map(int, input().split())))

  minSpeed = 0
  maxSpeed = 10**9
  for i in range(n):
    minSpeed = max(minSpeed, (i + 1)/max(0.000001, lst[i][1]))
    maxSpeed = min(maxSpeed, (i + 1)/max(0.000001, lst[i][0]))
  
  if minSpeed > maxSpeed:
    ans = -1
  else:
    ans = minSpeed
  
  print(f"Case #{__ + 1}: {ans}")