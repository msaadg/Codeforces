for __ in range(int(input())):
    s = list(input())
    ss = sorted(s)

    if s == ss:
        print(1)
    else:
        flag = False if s[0] == '0' else True
        usedup = False
        count = 1
        for c in s:
            if c == '1':
                if not flag and not usedup:
                    usedup = True
                elif not flag and usedup:
                    count += 1
                flag = True
            else:
                if flag:
                    count += 1
                flag = False
        print(count)