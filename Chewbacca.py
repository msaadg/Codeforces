x=input()
ans=''
for i in range(len(x)):
    if i==0 and 4<int(x[i])<9 or i!=0 and int(x[i])>4:
        ans+=str(9-int(x[i]))
    else:
        ans+=x[i]
print(ans)