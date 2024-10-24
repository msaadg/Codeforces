def SieveOfEratosthenes(n):
  prime = [True for i in range(n+1)]
  p = 2
  while (p * p <= n):
    if (prime[p] == True):
      for i in range(p * p, n+1, p):
        prime[i] = False
    p += 1
  return prime

for __ in range(int(input())):
  n = int(input())
  if n < 5:
    print(f"Case #{__ + 1}: 0")
    continue

  primes = SieveOfEratosthenes(n)
  primes[0] = False
  primes[1] = False
  ans = 1
  for i in range(5, len(primes)):
    if primes[i] and primes[i - 2]:
      ans += 1
  print(f"Case #{__ + 1}: {ans}")