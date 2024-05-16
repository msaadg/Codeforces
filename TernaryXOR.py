for __ in range(int(input())):
    n=int(input())
    x=input()
    str1=''
    str2=''
    str1flag=False
    for i in x:
        if i=='2':
            if str1flag==False:
                str1+='1'
                str2+='1'
            else:
                str1+='0'
                str2+='2'
        elif i=='1':
            if str1flag==False:
                str1+='1'
                str2+='0'
                str1flag=True
            else:
                str1+='0'
                str2+='1'
        elif i=='0':
            str1+='0'
            str2+='0'
    print(str1)
    print(str2)