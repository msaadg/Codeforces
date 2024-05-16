for __ in range(int(input())):
    n,c,q=map(int, input().split())
    s=input()
    d={}
    for i in range(c):
        l,r=map(int, input().split())
        n+=r-l+1
        d[n]=r
    for i in range(q):
        qy=int(input())
        while qy>len(s):
            for i in d:
                if i>=qy:
                    qy=d[i]-(i-qy)
                    break
        print(s[qy-1])