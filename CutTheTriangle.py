for __ in range(int(input())):
    input()
    x1,y1=map(int, input().split())
    x2,y2=map(int, input().split())
    x3,y3=map(int, input().split())
    if x1==x2 or x1==x3 or x2==x3:
        if y1==y2 or y1==y3 or y2==y3:
            print('NO')
            continue
    print('YES')