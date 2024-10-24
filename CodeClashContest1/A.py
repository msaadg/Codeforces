for __ in range(int(input())):
  s = input()
  if len(s) < 3:
    print("no")
  else:
    if s[0:2] == "10" and int(s[2:]) >= 2 and int(s[2]) != 0:
      print("yes")
    else:
      print("no")