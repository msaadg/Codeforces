def compute_pisano_period(k):
  F_prev, F_curr = 0, 1
  period = 0
  while True:
    F_prev, F_curr = F_curr, (F_prev + F_curr) % k
    period += 1
    if F_prev == 0 and F_curr == 1:
      break
  return period

print(compute_pisano_period(10**5))