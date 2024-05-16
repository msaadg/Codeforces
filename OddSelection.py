for __ in range(int(input())):
    n,x=map(int, input().split())
    a=list(map(int, input().split()))
    oddc,evenc=0,0
    for i in range(n):
        if a[i]%2==1:
            oddc+=1
        else:
            evenc+=1
    if oddc>=x and x%2==1:
        print('Yes')
    elif oddc>=x-1 and x%2==0 and evenc>=1:
        print('Yes')
    elif 1<=oddc<x and evenc>=x-oddc and oddc%2==1:
        print('Yes')
    elif 1<=oddc<x and evenc>=x-oddc+1 and oddc%2==0:
        print('Yes')
    else:
        print('No')