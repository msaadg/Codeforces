for __ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    pntr1=0
    pntr2=1
    count=0
    while pntr1<n and pntr2<n:
        if a[pntr1]==a[pntr2]:
            count+=pntr2-pntr1
            pntr1=pntr2
            pntr2+=1
        else:
            pntr2+=1
    print(n-count)