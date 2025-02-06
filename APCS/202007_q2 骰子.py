class dice:
  def __init__(self, front: int, left: int, top: int):
    self.front = front
    self.left = left
    self.top = top 
    
  def update_front(self):
    f = self.front
    t = self.top
    self.front = t
    self.top = 7 - f 

  def update_right(self):
    t = self.top 
    l = self.left
    self.top = l
    self.left = 7 - t 

n, m = map(int, input().split())
L = [dice(4,5,1) for _ in range(n+1)]

for _ in range(m):
  a,b = map(int, input().split())
  if b == -1:
    L[a].update_front()
  elif b == -2:
    L[a].update_right()
  else:
    L[a], L[b] = L[b], L[a]
    
for i in range(1, n+1):
  print(L[i].top, end = " ")
