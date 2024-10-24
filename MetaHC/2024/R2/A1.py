import math
lst = []
cnt = 0
for i in range(19):
  if i % 2 == 0:
    cnt += 1
    for j in range(10 - cnt):
      s = len(str(10 ** i))
      st = ''
      for k in range(s // 2):
        st += str(k + j + 1)
      st2 = st[::-1]
      st += str(s//2 + j + 1)
      st += st2
      lst.append(int(st))

# print(len(lst))

for __ in range(int(input())):
  a, b, m = map(int,input().split())
  ans = 0
  for i in lst:
    if a <= i <= b and i % m == 0:
      ans += 1
  print(f"Case #{__ + 1}: {ans}")