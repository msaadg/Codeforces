import math
from collections import Counter
for __ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))

  d = Counter(a[:n])
  m = max(d.values())
  
  i = math.ceil(math.log(n/m) / math.log(2))
  print(i + (n - m))