n=int(input())
lst=list(map(int, input().split()))
odd,even=[],[]
for i in range(n):
    if lst[i]%2==0:
        even.append(i+1)
    else:
        odd.append(i+1)
if len(even)==1:
    print(even[0])
else:
    print(odd[0])