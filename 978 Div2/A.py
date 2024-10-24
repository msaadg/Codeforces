for __ in range(int(input())):
  n, r = map(int, input().split())
  a = list(map(int, input().split()))

  singles = 0
  doubles = 0
  for i in range(n):
    doubles += a[i] // 2
    if a[i] % 2 == 1:
      singles += 1
  
  rem = r - doubles
  h = singles if rem >= singles else 2 * rem - singles
  print(doubles * 2 + h)