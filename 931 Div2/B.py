for __ in range(int(input())):
    n = int(input())
    # read a.txt which is like this [1, 2, 3, 4, 5, ... 10**9]
    # the ans is the nth index in a.txt

    # read a.txt
    with open('a.txt', 'r') as f:
        data = f.read()
        data = data[1:-1]
    # convert data to list
    data = data.split(', ')
    # convert data to int
    data = list(map(int, data))
    # print the nth index
    print(data[n])
