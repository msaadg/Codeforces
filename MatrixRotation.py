for __ in range(int(input())):
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    if max(a,b,c,d)-min(a,b,c,d)==abs(a-d) or max(a,b,c,d)-min(a,b,c,d)==abs(b-c):
        print('yes')
    else:
        print('no')