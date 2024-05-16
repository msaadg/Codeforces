for __ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if n==1:
        print("No")
    else:
        count1 = 0
        count = 0
        for i in range(n):
            if a[i]==1:
                count1+=1
            else:
                count+=a[i] - 1
        if count>=count1:
            print("Yes")
        else:
            print("No")