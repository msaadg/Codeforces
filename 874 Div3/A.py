for __ in range(int(input())):
    n=int(input())
    s=input()
    lst=[s[0:2]]
    for i in range(1,len(s)-1):
        if s[i]+s[i+1] not in lst:
            lst.append(s[i]+s[i+1])
    print(len(lst))