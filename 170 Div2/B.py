pow2 = [1] * (10**5 + 1)
for k in range(1, 10**5 + 1):
  pow2[k] = (pow2[k - 1] * 2) % (10**9 + 7)

t = int(input())
n = list(map(int, input().split()))
k = list(map(int, input().split()))

for i in k:
    print(pow2[i])
