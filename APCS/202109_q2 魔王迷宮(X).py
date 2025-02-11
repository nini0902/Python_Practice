from dataclasses  import dataclass

class Boss:
  def __init__(self, x, y, nx, ny, status):
    self.nx = nx
    self.ny = ny 
    self.x = x 
    self.y = y
    self.status = status
  
  def move(self):
    self.nx += self.x
    self.ny += self.y

n,m,k = map(int, input().split())
bomb = [[0] * m for _ in range(n)]
cnt_bomb = k
boss = []
for _ in range(k):
  r,c,s,t = map(int, input().split())
  boss.append(Boss(r,c,s,t, 1))
  bomb[r][c] = 1

explode = []

while k:
  for b in boss:
    if b.status != 1: continue
    b.move()
    
    # 檢查有沒有超出範圍
    if b.nx >= n or b.nx < 0 or b.ny >= m or b.ny < 0:
      b.status = -1
      k -= 1
      
    if b.status == -1: continue
    
    # 檢查有沒有踩到地雷
    if bomb[b.nx][b.ny]:
      k -= 1
      b.status = 0
      
  for b in boss:
    if b.status == 0 and bomb[b.nx][b.ny] == 1: 
      bomb[b.nx][b.ny] = 0
      cnt_bomb -= 1
    elif b.status == -1: continue
  
    if b.status == 1 and bomb[b.nx][b.ny] == 0:
      cnt_bomb += 1
      bomb[b.nx][b.ny] = 1
print(cnt_bomb)
