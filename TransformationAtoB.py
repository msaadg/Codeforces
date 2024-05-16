a,b=map(int, input().split())
lst=[b]
while b>a:
    if b%10==1:
        b//=10
    elif b%2!=0:
        break
    else:
        b//=2
    lst.append(b)
lst.reverse()
print('YES'+'\n'+str(len(lst))+'\n'+' '.join(map(str, lst)) if a==b else 'NO')