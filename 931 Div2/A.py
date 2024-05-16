for __ in range(int(input())):
    n = int(input())
    lst = sorted(list(map(int, input().split())))
    
    print(abs(lst[-1] - lst[0]) + abs(lst[-2] - lst[1]) +
          abs(lst[-1] - lst[1]) + abs(lst[-2] - lst[0]))
    