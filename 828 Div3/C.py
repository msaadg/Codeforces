for __ in range(int(input())):
    n,c=input().split()
    s=input()
    s*=2
    x,y=0,0
    for i in range(len(s)-1,-1,-1):
        x+=1
        if s[i]=='g':
            x=0
        elif s[i]==c:
            y=max(y,x)
    print(y)