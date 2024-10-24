for __ in range(int(input())):
  n, m, k = map(int, input().split())
  a = input()

  logs = [0]

  for i in range(n):
    if a[i] == 'L':
      logs.append(i + 1)
  
  logs.append(n + 1)
  
  swmFlag = False
  swm = 0
  cFlag = False

  for i in range(1, len(logs)):
    if logs[i] - logs[i - 1] > m or swmFlag:
      swmFlag = True
      for j in range(logs[i - 1] + m, logs[i]):
        if a[j - 1] == 'W':
          swm += 1
        else:
          cFlag = True

  if cFlag or swm > k:
    print("no")
  else:
    print("yes")
  