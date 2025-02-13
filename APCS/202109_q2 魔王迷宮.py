n, m, k = map(int, input().split())
bomb = [[0] * m for _ in range(n)]
boss = []

for _ in range(k):
    r, c, s, t = map(int, input().split())
    boss.append([r, c, s, t, 1])  
    bomb[r][c] = 1

while k:
  explode = []
  for i in range(len(boss)):
    if boss[i][4] != 1:
      continue
        
    boss[i][0] += boss[i][2]
    boss[i][1] += boss[i][3]
        
    # 檢查有沒有超出範圍
    if boss[i][0] >= n or boss[i][0] < 0 or boss[i][1] >= m or boss[i][1] < 0:
      boss[i][4] = -1
      k -= 1
        
    if boss[i][4] == -1:
      continue
        
    # 檢查有沒有踩到地雷
    if bomb[boss[i][0]][boss[i][1]]:
      k -= 1
      boss[i][4] = 0
      explode.append((boss[i][0], boss[i][1]))
            
  for x,y in explode:
    bomb[x][y] = 0
  for i in range(len(boss)):
    if boss[i][4] == 1:
      bomb[boss[i][0]][boss[i][1]] = 1

cnt_bomb = sum(row.count(1) for row in bomb)
print(cnt_bomb)
