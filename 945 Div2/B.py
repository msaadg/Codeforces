import math

def lonely(x):
    m = max(1, max(a))
    l = int(math.log2(m)) + 1
    bits = [0] * l

    for i in range(x):
        for j in range(l):
            if a[i] & (1 << j):
                bits[j] += 1

    or_value = 0
    for i in range(l):
        if bits[i] > 0:
            or_value += 2 ** i

    for i in range(1, n - x + 1):
        for j in range(l):
            if a[i - 1] & (1 << j):
                bits[j] -= 1

        for j in range(l):
            if a[i + x - 1] & (1 << j):
                bits[j] += 1
        
        current_or = 0
        for j in range(l):
            if bits[j] > 0:
                current_or += 2 ** j
        
        if current_or != or_value:
            return False
        
    return True

for __ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    l = 1
    r = n
    while l <= r:
        mid = (l + r) // 2
        if lonely(mid):
            r = mid - 1
        else:
            l = mid + 1
    
    print(l)