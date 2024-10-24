for __ in range(int(input())):
  n = int(input())
  s = input()

  if s[0] == '1' or s[-1] == '1' or '11' in s:
    print('yes')
  else:
    print('no')