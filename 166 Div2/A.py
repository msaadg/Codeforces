for __ in range(int(input())):
  n = int(input())
  s = input()

  flag = True
  lastdigit = '0'
  lastletter = 'a'

  letter = False
  for c in s:
    # if number
    if c.isdigit():
      if c < lastdigit or letter:
        flag = False
        break
      lastdigit = c
    else:
      letter = True
      if c < lastletter or c.isupper():
        flag = False
        break
      lastletter = c

  if flag:
    print("YES")
  else: 
    print("NO")