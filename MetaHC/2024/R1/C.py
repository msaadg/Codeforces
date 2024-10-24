def backtrack(curw, minw, g, l, lvl, prob, lim):
  if lim > 40:
    return
  if curw == g:
    lst.append(prob * lvl)
    return
  
  if curw == minw + l:
    backtrack(curw - 1, min(minw, curw - 1), g, l, lvl + 1, prob, lim)
  else:
    backtrack(curw - 1, min(minw, curw - 1), g, l, lvl + 1, prob * 1/2, lim + 1)
    backtrack(curw + 1, minw, g, l, lvl + 1, prob * 1/2, lim + 1)


for __ in range(int(input())):
  w, g, l = map(int, input().split())
  lst = []
  if l == 0:
    print(f"Case #{__ + 1}: {(w - g) % 998244353}")
  else:
    backtrack(w, w, g, l, 0, 1, 0)
    print(f"Case #{__ + 1}: {round(sum(lst)) % 998244353}")