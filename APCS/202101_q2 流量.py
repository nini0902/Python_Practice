n,m,k = map(int, input().split())
Q = [[0] * m for _ in range(n)]

for i in range(n):
  L = list(map(int, input().split()))
  for j in range(m):
    Q[i][j] = L[j]
  
cost = [0 for _ in range(k)]

for K in range(k):
  c = list(map(int, input().split()))
  tt = [[0 for i in range(m)] for j in range(m)]
  
  for i in range(n):
    for j in range(m):
      tt[c[i]][j] += Q[i][j]
  
  for i in range(m):
    for j in range(m):
      if i == j:
        cost[K] += tt[i][j]
      elif tt[i][j] <= 1000:
        cost[K] += tt[i][j] * 3
      else:
        cost[K] += (tt[i][j]-1000)*2 + 3000
        
print(min(cost))
