k = int(input())
s = input()
cnt = 0
L = []

if s[0].isupper(): ul = 1
else: ul = 0

for i in s:
  if i.isupper() and ul == 1: cnt += 1
  elif i.islower() and ul == 0: cnt += 1
  else:
    L.append(cnt)
    cnt = 1
    ul = ul^1
L.append(cnt)

ans = 0
cnt = 0
last = 0

for i in L:
  if i > k:
    ans = max(cnt+1, ans)
    cnt = 1
  elif i == k:
    cnt += 1 
  else:
    ans = max(cnt, ans)
    cnt = 0
    last = 0
ans = max(cnt, ans)
print(ans * k)
