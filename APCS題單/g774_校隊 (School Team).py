def comp(x):
  b,g = x
  return b-g

n,m = map(int, input().split())

l = []
for i in range(n+m):
  b,g = [int(x) for x in input().split()]
  l.append([b,g])
  
l.sort(key=comp) #用男比女快多少排

time = 0
#男快女最多的n個班
for i in range(0, n):
  time += l[i][0]
#最後才選女生
for i in range(n, n+m):
  time += l[i][1]
  
print(time)
