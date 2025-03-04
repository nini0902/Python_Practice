n = int(input())

for _ in range(n):
  s = input()
  cnt = 0
  for c in s:
    if c == "(": 
      cnt += 1 
    elif c == ")": 
      cnt -= 1 
    
    if cnt < 0:
      cnt = -1
      break
  if cnt != 0: print(0)
  else: print(len(s)//2)
