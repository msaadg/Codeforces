for __ in range(int(input())):
    n = int(input())
    s = input()
    f = input()
    rem = 0
    add = 0

    for i in range(n):
        # remove
        if s[i] == '1' and f[i] == '0':
            rem += 1

        # add
        elif s[i] == '0' and f[i] == '1':
            add += 1
    
    print(max(rem, add))