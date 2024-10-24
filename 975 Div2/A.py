for __ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))

  o = []
  e = []
  for i in range(n):
    if i % 2 == 0:
      e.append(a[i])
    else:
      o.append(a[i])
    
  if len(o) == 0:
    print(sum(e) + len(e))
  elif len(e) == 0:
    print(sum(o) + len(o))
  else:
    print(max(o) + len(o) if max(o) + len(o) > max(e) + len(e) else max(e) + len(e))