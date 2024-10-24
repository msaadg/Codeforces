import math

x = int(input())

ans = 0
while x > 1:
  if x % 2 == 0:
    x //= 2
  else:
    x -= 1
    ans += 1

print(ans + 1)