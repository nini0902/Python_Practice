n,k = map(int, input().split())
x = list(map(int, input().split()))
x.sort()

d = [10**10] * n #儲存第一場會議移動的距離

# 計算第一場會議總和
d[k-1] = sum(abs(i-x[k//2]) for i in x[:k])

l, mid = 1, k//2+1 
for r in (k, n):
  d[r] = d[r-1] - (x[mid] - x[l]) # 減掉最左邊離開窗口的人
  d[r] += x[r] - x[mid] # 計算最新加入到中點距離
  d[r] += (x[mid] - x[mid-1]) * (mid-l-(r-mid)) # 計算新的中點帶來的影響
  l += 1 
  mid += 1 

