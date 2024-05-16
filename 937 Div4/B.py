for __ in range(int(input())):
    n = int(input())

    flagH = True
    flagV = True
    for i in range(2*n):
        if flagV:
            flagH = True
        else:
            flagH = False

        for j in range(n):
            if flagH:
                print("##", end="")
            else:
                print("..", end="")
            flagH = not flagH
        if i % 2 == 1:
            flagV = not flagV
        print()