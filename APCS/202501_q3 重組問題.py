n = int(input())
d = sorted([int(x) for x in input().split()])

# 只有一個數字
if n == 1:
  print(0); print(0)
  exit(0)
  
imax = [0] * n # 最大序列
imin = [1000] * n  # 最大序列
M = d[-1] #目前最大數字
p = [0] #儲存所有數列

# point 是目前還原的數組
# dis 是還原目前數組還剩下的絕對值
def dfs(point, dis, q):
  global imin, imax
  # 檢查欲新增的數字q符不符合
  for v in point:
    q_dis = abs(q - v)
    if q_dis not in dis:
      return 
    dis.remove(q_dis)
    
  point.append(q)
  if not dis: # 找到其中一組數組
    point.sort()
    imin = min(imin, point)
    imax = max(imax, point)
    return
  
  # 繼續查找下一個可能值直到結束
  q = dis[-1]
  dfs(point[:], dis[:], q)
  dfs(point[:], dis[:], M - q)
  return 

dfs(p,d,M)
print(*imin)
print(*imax)
