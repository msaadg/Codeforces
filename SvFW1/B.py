s = input()
t = input()

slen = len(s)
tlen = len(t)

pntr = -1

while (slen + pntr > - 1) and (tlen + pntr > - 1) and s[pntr] == t[pntr]:
    pntr -= 1

print(slen + pntr + tlen + pntr + 2)