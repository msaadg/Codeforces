for __ in range(int(input())):
  x, y, k = map(int, input().split())
  if k % 2 == 1:
    print(x, y)
  for i in range(1, k//2 + 1):
    print(x+i, y+i)
    print(x-i, y-i)