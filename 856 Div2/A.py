for __ in range(int(input())):
    n=int(input())
    lst=input().split()
    x,y='',''
    for i in lst:
        if len(i)==n-1:
            if x=='':
                x=i
            else:
                y=i
    suffix=[*x]
    prefix=[*y]
    if suffix[1:]==prefix[:n-2]:
        suffix.append(prefix[-1])
        r=suffix[:]
        suffix.reverse()
        if r==suffix:
            print('Yes')
        else:
            print('No')
    elif prefix[1:]==suffix[:n-2]:
        prefix.append(suffix[-1])
        r=prefix[:]
        prefix.reverse()
        if r==prefix:
            print('Yes')
        else:
            print('No')