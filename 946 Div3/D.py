for __ in range(int(input())):
    n = int(input())
    s = input()

    r = [0, 0]      # r[0] = x, r[1] = y
    h = [0, 0]      # h[0] = x, h[1] = y
    lst = []
    s1 = set()
    flag = True
    for i in range(n):
        if s[i] == 'N':
            if r[1] == h[1]:
                if flag:
                    r[1] += 1
                    lst.append('R')
                    s1.add('R')
                    flag = False
                else:
                    h[1] += 1
                    lst.append('H')
                    s1.add('H')
            elif r[1] < h[1]:
                r[1] += 1
                lst.append('R')
                s1.add('R')
            else:
                h[1] += 1
                lst.append('H')
                s1.add('H')
        elif s[i] == 'S':
            if r[1] == h[1]:
                if flag:
                    r[1] -= 1
                    lst.append('R')
                    s1.add('R')
                    flag = False
                else:
                    h[1] -= 1
                    lst.append('H')
                    s1.add('H')
            elif r[1] > h[1]:
                r[1] -= 1
                lst.append('R')
                s1.add('R')
            else:
                h[1] -= 1
                lst.append('H')
                s1.add('H')
        elif s[i] == 'E':
            if r[0] == h[0]:
                if flag:
                    r[0] += 1
                    lst.append('R')
                    s1.add('R')
                    flag = False
                else:
                    h[0] += 1
                    lst.append('H')
                    s1.add('H')
            elif r[0] < h[0]:
                r[0] += 1
                lst.append('R')
                s1.add('R')
            else:
                h[0] += 1
                lst.append('H')
                s1.add('H')
        else:                           # s[i] == 'W'
            if r[0] == h[0]:
                if flag:
                    r[0] -= 1
                    lst.append('R')
                    s1.add('R')
                    flag = False
                else:
                    h[0] -= 1
                    lst.append('H')
                    s1.add('H')
            elif r[0] > h[0]:
                r[0] -= 1
                lst.append('R')
                s1.add('R')
            else:
                h[0] -= 1
                lst.append('H')
                s1.add('H')

    if r[0] == h[0] and r[1] == h[1] and len(s1) == 2:
        print("".join(lst))
    else:
        print('NO')