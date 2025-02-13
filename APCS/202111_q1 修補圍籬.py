n = int(input())
h = list(map(int, input().split()))

cost = 0
for i in range(len(h)):
  if h[i] > 0: # 圍籬是完好的
    continue
  
  if h[i] == 0:
    if i == 0:
      cost += h[1]
    elif i == len(h)-1:
      cost += h[len(h)-2]
    else:
      cost += min(h[i-1], h[i+1])
      
print(cost)
