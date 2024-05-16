n,l=map(int, input().split())
a=sorted(list(map(int, input().split())))
first=a[0]
last=a[-1]
maxdiff=max(first-0, l-last)
for i in range(n-1):
    if (a[i+1]-a[i])/2>maxdiff:
        maxdiff=(a[i+1]-a[i])/2
print(maxdiff)