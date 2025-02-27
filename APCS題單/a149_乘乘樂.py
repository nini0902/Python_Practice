n = int(input())
for _ in range(n):
  s = list(input())
  cnt = 1 
  for i in s:
    cnt *= int(i)
  print(cnt)
