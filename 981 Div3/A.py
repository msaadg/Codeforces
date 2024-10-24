for __ in range(int(input())):
  n = int(input())
  ans = 0
  pos = 0
  c = 1

  while pos <= n and pos >= -n:
    # print(pos)
    pos += c if ans == 0 else -c
    ans = 0 if ans == 1 else 1
    c += 2
  
  print("Sakurako" if ans == 1 else "Kosuke")