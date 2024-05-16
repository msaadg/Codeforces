for __ in range(int(input())):
    n,k=map(int,input().split())
    c=list(map(int,input().split()))
    start, end = c[0], c[n-1]
    pntr1, pntr2 = 0, n-1
    kstart, kend = k, k
    while pntr1<pntr2 and (kstart>0 or kend>0):
        if c[pntr1]==start and kstart>0:
            kstart-=1
        if kstart>0:
            pntr1+=1
        if c[pntr2]==end and kend>0:
            kend-=1
        if kend>0:
            pntr2-=1
    
    if kstart==0 and kend==0:
        print("YES")
    else:
        if start==end and (k-kstart)==kend and (k-kend)==kstart:
            print("YES")
        elif c[pntr1]==c[pntr2] and c[pntr1]==start and c[pntr2]==end:
            print("YES")
        else:
            print("NO")
