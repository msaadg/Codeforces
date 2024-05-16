n = input()

if n[0] != '1':
    print("NO")
else:
    flag = True
    count4 = 0
    for i in n:
        if i != '1' and i != '4':
            print("NO")
            flag = False
            break
        elif i == '4':
            count4 += 1
            if count4 > 2:
                print("NO")
                flag = False
                break
        elif i == '1':
            count4 = 0
    if flag: print("YES")