for __ in range(int(input())):
    n=int(input())
    s=input()
    i=0
    flag=True
    while i<len(s):
        if i%3==0:
            i+=1
        else:
            if i==len(s)-1 or s[i]!=s[i+1]:
                flag=False
                break
            else:
                i+=2
    if flag==True:
        print('YES')
    else:
        print('NO')