a,b = map(int, input().split())
n = int(input())

L = []
cnt = 0

for _ in range(n):
  A,B = 0,0
  L = list(map(int, input().split()))
  
  for i in L:
    if i == a: A += 1 
    elif i == -a: A -= 1 
    
    if i == b: B += 1 
    elif i == -b: B -= 1
    
  if A>0 and B>0: cnt += 1 
  
print(cnt)
