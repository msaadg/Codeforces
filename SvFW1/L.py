for __ in range(int(input())):
    n = int(input())
    s = input().lower()
    
    d = {'m':['m'], 'e':['m', 'e'], 'o':['e', 'o'], 'w':['o', 'w']}

    if s[0] != 'm' or s[-1] != "w":
        print("No")
    else:
        flag = True
        for i in range(1, n):
            if s[i] not in d or (s[i - 1] not in d[s[i]]):
                print("No")
                flag = False
                break
        if flag: print("Yes")