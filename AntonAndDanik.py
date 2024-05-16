n=int(input())
s=input()
if s.count('A')==n/2:
    print('Friendship')
elif s.count('A')>n/2:
    print('Anton')
else:
    print('Danik')