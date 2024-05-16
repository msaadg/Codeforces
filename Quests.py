for __ in range(int(input())):
    n,c,d=map(int, input().split())
    a=sorted(list(map(int, input().split())),reverse=True)
    sumlst=[0]
    for i in a:
        sumlst.append(sumlst[-1]+i)
    ans="Impossible"
    for k in range(d + 1):
        if sumlst[min(n,k+1)]*(d//(k+1))+sumlst[min(n,d%(k+1))]>=c:
            ans=k
    print("Infinity" if ans==d else ans)