for __ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    odd=[]
    even=[]
    oddcount=0
    evencount=0
    for i in range(n):
        if a[i]%2==1:
            odd.append(i+1)
            oddcount+=1
        else:
            even.append(i+1)
            evencount+=1
    if 1<=oddcount<=2 and evencount>=2 or oddcount>=3:
        print('YES')
        if oddcount>=3:
            print(odd[0],odd[1],odd[2])
        elif 1<=oddcount<=2 and evencount>=2:
            print(odd[0],even[0],even[1])
    else:
        print('NO')