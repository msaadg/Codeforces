import math
r,g,b=map(int, input().split())
r,g,b=math.ceil(r/2),math.ceil(g/2),math.ceil(b/2)
maxval=max(r,g,b)
if r==maxval:
    time=0
if g==maxval:
    time=1
if b==maxval:
    time=2
print(time+3*(maxval-1)+30)