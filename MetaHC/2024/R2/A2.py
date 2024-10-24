import math

def construct_first(start, end, i, s):
  if start > 8 or end < 1 or len(s) == len(10 ** i) // 2:
    return



lst = []
for i in range(19):
  if i % 2 == 0:
    for j in range(1, 9):
      for k in construct_first
print(lst)

for __ in range(int(input())):
  a, b, m = map(int,input().split())
  ans = 0
  for i in lst:
    if a <= i <= b and i % m == 0:
      ans += 1
  print(ans)