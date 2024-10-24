import math
for __ in range(int(input())):
  x, y, k = map(int, input().split())
  xans = math.ceil(x/k)
  yans = math.ceil(y/k)
  if xans > yans:
    print(xans + xans - 1)
  else:
    print(max(xans, yans) * 2)