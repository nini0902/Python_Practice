n = int(input())
line = []

for _ in range(n):
  a,b = map(int, input().split())
  line.append((a,b))
  
line.sort(key=lambda x:(x[0], x[1]))

cnt = 0; l = -1; r = -1
for i in range(n):
  if line[i][0] <= l and line[i][1] <= r:
    continue
  if line[i][0] > r:
    cnt += r-l
    l = line[i][0]
  if line[i][1] >= r:
    r = line[i][1]
cnt += r-l
  
print(cnt)
