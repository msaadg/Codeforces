s=input()
word='hello'
a=0
for i in s:
    if i==word[a]:
        a+=1
        if a>=5:
            print('YES')
            quit()
print('NO')