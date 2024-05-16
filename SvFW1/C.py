import math
n = int(input())
a = sorted(list(map(int, input().split())))

d1, d2 = {}, {}

for i in range(n):
    d1[a[i]] = d1.get(a[i], 0) + 1
    d2[a[i]] = d2.get(a[i], 0) + 1
    if math.log2(a[i]) % 1 == 0:
        find = a[i]
        if d1[find] > 1:
            d2[find] = 0
    else:
        find = 2**math.ceil(math.log2(a[i])) - a[i]
        if find in d1:
            d2[find] = 0
            d2[a[i]] = 0
print(sum(d2.values()))