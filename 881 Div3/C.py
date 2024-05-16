for __ in range(int(input())):
    n=int(input())
    count=0
    while n!=1:
        count+=n
        n=n//2
    print(count+1)