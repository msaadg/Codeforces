str1=input().lower()
str2=input().lower()
for i in range(len(str1)):
    if str1[i]>str2[i]:
        print(1)
        quit()
    elif str1[i]<str2[i]:
        print(-1)
        quit()
print(0)