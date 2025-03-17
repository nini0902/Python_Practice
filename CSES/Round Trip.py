# DFS
import sys
sys.setrecursionlimit(10**6)

def dfs(start, pre):
  visited[start] = True # visited
  for i in adj[start]:
    if i == pre: 
      continue
  
    if visited[i]:
      path.append(start)
      node  = start
      while node != i:
        path.append(p[node])
        node = p[node]
      path.append(start)
      
      print(len(path))
      print(" ".join(map(str, path[::-1])))
      exit()
      
    p[i] = start
    if dfs(i, start):
      return True
  return False
      
 
n,m = map(int, input().split())
 
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [False] * (n+1)
p = [-1] * (n+1)
path = []
 
for i in range(1, n+1):
  if not visited[i]:
    if dfs(i, -1):
      break
      
print("IMPOSSIBLE")
