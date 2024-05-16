for __ in range(int(input())):
    n,k=map(int, input().split())
    p=sorted(list(map(int, input().split())), reverse=True)
    lst=[]
    count=0
    ans = 0
    while count<len(p):
        lst.append(p[count])
        count += 1
        if count % k == 0:
            ans = max(ans, sum(lst[-(count//k):]))
    print(ans)
