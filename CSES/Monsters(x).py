from collections import deque
dir = [(0,-1), (1,0), (0,-1), (-1,0)] # u, r, d, l

def bfs(nx, ny):
  queue = deque([(nx, ny)]) # 把 list 變成 deque
  visited = set() # 更有效率的查找
  visited.add((nx, ny))
  
  while queue:
    x,y = queue.popleft()
    
    for dx, dy in dir:
      nx, ny = x+dx, y+dy
      if 0 <= nx < n and 0 <= ny < m and (nx,ny) not in visited and lab[nx][ny] == 0:
        queue.append((nx,ny))
        visited.add((nx,ny))
  return visited

n, m = map(int, input().split())
lab = [[0]*m for _ in range(n)]

for i in range(n):
  lab[i] = list(input().strip())
  for j in range(m):
    c = lab[i][j]
    if c == "#" or c == "M":
      lab[i][j] = -1
    else:
      lab[i][j] = 0
      
    if c == "A":
      x,y = i, j
      
print(bfs(x,y))
