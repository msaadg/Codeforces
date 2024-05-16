for _ in range(int(input())):
    s=input()
    if s[1]=='a':
        print(s[0],s[1],s[2:])
    elif s[1]=='b':
        print(s[0],s[1:-1],s[-1])
