n, k = map(int, input().split())
a = list(map(int, input().split()))

m = sum(a[:k])
ans = 1

i = 0
j = k
curr = m
while j < n:
  curr = curr - a[i] + a[j]
  if curr < m:
    ans = i + 2
    m = curr
  i += 1
  j += 1

print(ans)