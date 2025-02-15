M,N,k,r,c = map(int, input().split())
m = [list(map(int,  input().split())) for _ in range(M)]
  
d = 0
direction = ((0,1), (1,0), (0,-1), (-1,0))
score = 0
dim = 0 # 收集寶石的數量

while m[r][c] != 0:
  score += m[r][c]
  dim += 1 
  m[r][c] -= 1 
  move = False
  turn = 0 #因為分數而轉向(最多就一次)
  
  while not move:
    nr, nc = r+direction[d][0], c+direction[d][1]
    if score % k == 0 and turn == 0:
      d = (d+1)%4
      turn = 1 
    elif (d == 0 and nc >= N) or (d == 1 and nr >= M) or (d == 2 and nc < 0) or (d == 3 and nr < 0):
      d = (d+1)%4
    elif m[nr][nc] == -1:
      d = (d+1)%4
    else:
      move = True
      r,c = nr, nc
      
print(dim)
