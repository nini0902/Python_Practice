n,k = map(int, input().split())
x = list(map(int, input().split()))
x.sort()

d = [10**10] * n #儲存第一場會議移動的距離

# 計算第一場會議總和
d[k-1] = sum(abs(i-x[k//2]) for i in x[:k])

l, mid = 1, k//2+1 
for r in range(k, n):
  d[r] = d[r-1] - (x[mid-1] - x[l-1]) # 減掉最左邊離開窗口的人
  d[r] += x[r] - x[mid] # 計算最新加入到中點距離
  d[r] += (x[mid] - x[mid-1]) * (mid-l-(r-mid)) # 計算新的中點帶來的影響
  l += 1 
  mid += 1 
  
pmin = d[:]
# d[i] 表示從 i-k+1 到 i 這 k 人作為第一場會議的最小移動距離
for i in range(k, n):
  # 快速查找第一場會議的最佳方案
  pmin[i] = min(pmin[i], pmin[i-1])

# d[i] 代表以 i 為最後一人的 k 人，做為第二場會議的最小移動距離
# pmin[i-k] 代表第一場會議在 i-k 之前最佳選擇
best = min(d[i]+pmin[i-k] for i in range(k+k-1, n))
  
print(best)
