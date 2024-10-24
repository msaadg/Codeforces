s = input().lower()
ans = ""
for c in s:
  if c == "a" or c == "e" or c == "i" or c == "o" or c == "u" or c == "y":
    continue
  else:
    ans += "." + c

print(ans)