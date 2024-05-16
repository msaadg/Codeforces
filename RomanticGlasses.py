# for __ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))

#     d = set([0])
#     s = 0
#     for i in range(n):
#         s += a[i] if i % 2 else -a[i]
#         d.add(s)
#     print("YES" if len(d) <= n else "NO")


for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    s = 0
    d = set([0])
    for i in range(n):
        s += lst[i] if i % 2 == 0 else -lst[i]
        d.add(s)
    if len(d) <= n:
        print("YES")
    else:
        print("NO")