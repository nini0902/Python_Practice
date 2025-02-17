n = int(input())
adj = [[] for i in range(n)]
for i in range(n-1):
  s,t = map(int,input().split())
  adj[s].append(t)
  adj[t].append(s)
  
def bfs(s):
  d = [-1]*n # 儲存與起點s的距離(-1表示未拜訪)
  que = [s]
  head = 0
  d[s] = 0
  
  while head < len(que):
    v = que[head]; head += 1
    for u in adj[v]:
      if d[u] < 0:
        d[u] = d[v] + 1 
        que.append(u)
  return que[-1], d[que[-1]]
  
v,_ = bfs(0)
u,diameter = bfs(v)
print(diameter)
