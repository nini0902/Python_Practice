from collections import deque 

def bfs(start):
  queue = deque([start]) # start with "start"
  team[start] = 1 # every new node start with team 1 
  
  while queue:
    node = queue.popleft()
    for neighbor in adj[node]:
      if team[neighbor] == 0:
        team[neighbor] = 3-team[node]
        queue.append(neighbor)
      elif team[neighbor] == team[node]:
        return False
  return True

n,m = map(int, input().split())

adj = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  adj[a].append(b)
  adj[b].append(a)

team = [0]*(n+1)

# make sure every node has gone through
possible = True
for i in range(1, n+1):
  if team[i] == 0:
    if not bfs(i):
      possible = False
      break 

if possible:
  for i in team[1:]:
    print(i, end = ' ')
else:
  print("IMPOSSIBLE")
