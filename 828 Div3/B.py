for __ in range(int(input())):
    n,q=map(int, input().split())
    a=list(map(int, input().split()))
    numeven=0
    numodd=0
    total=sum(a)
    for j in a:
        if j%2==0:
            numeven+=1
        else:
            numodd+=1
    for i in range(q):
        type,x=map(int,input().split())
        if type==0 and x%2==0:
            total+=numeven*x
            print(total)
        elif type==0 and x%2==1:
            total+=numeven*x
            print(total)
            numodd+=numeven
            numeven=0
        elif type==1 and x%2==0:
            total+=numodd*x
            print(total)
        elif type==1 and x%2==1:
            total+=numodd*x
            print(total)
            numeven+=numodd
            numodd=0


        # if type==0:
        #     for j in range(len(a)):
        #         if a[j]%2==0:
        #             a[j]+=x
        # else:
        #     for j in range(len(a)):
        #         if a[j]%2==1:
        #             a[j]+=x
        # print(sum(a))