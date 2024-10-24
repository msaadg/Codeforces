MOD = 10**9 + 7

def compute_z(k):
  if k == 1:
    return 1
  f0, f1 = 0, 1
  cnt = 1
  # cnt_max = 2 * k
  while True:
    f2 = (f0 + f1) % k
    f0, f1 = f1, f2
    cnt += 1
    if f0 == 0:
      return cnt - 1

import sys
input = sys.stdin.readline
t = int(input())
z_k_dict = {}
test_cases = []
for _ in range(t):
  n_str, k_str = input().split()
  n, k = int(n_str), int(k_str)
  test_cases.append((n, k))

k_set = set(k for n, k in test_cases)

for k in k_set:
  if k == 1:
    z_k_dict[k] = 1
  else:
    z_k_dict[k] = compute_z(k)

for n, k in test_cases:
  G_nk = (n * z_k_dict[k]) % MOD
  print(G_nk)
