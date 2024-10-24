for __ in range(int(input())):
  s = input()
  t = input()

  j = 0
  for i in range(min(len(s), len(t))):
    if s[i] == t[i]:
      j = i + 1
    else:
      break
  
  ans = len(t) + len(s)
  if j > 0:
    ans -= j
    ans += 1
  print(ans)