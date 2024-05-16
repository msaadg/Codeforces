for i in range(int(input())):
    hour, minutes = map(int, input().split(":"))

    # 24 hour to 12 hour

    if hour == 0:
        print("12:{:02d} AM".format(minutes))
    elif hour < 12:
        print("{:02d}:{:02d} AM".format(hour, minutes))
    elif hour == 12:
        print("12:{:02d} PM".format(minutes))
    else:
        print("{:02d}:{:02d} PM".format(hour - 12, minutes))