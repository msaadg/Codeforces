for __ in range(int(input())):
    Ax,Ay=map(int, input().split())
    Bx,By=map(int, input().split())
    Cx,Cy=map(int, input().split())
    bx=Ax-Bx
    by=Ay-By
    cx=Ax-Cx
    cy=Ay-Cy
    ans=1
    if bx>=0 and cx>=0:
        ans+=min(bx, cx)
    elif bx<0 and cx<0:
        ans+=min(-bx, -cx)

    if by>=0 and cy>=0:
        ans+=min(by, cy)
    elif by<0 and cy<0:
        ans+=min(-by, -cy)
    
    print(ans)