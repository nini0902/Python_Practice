n = int(input())

stu = []
for i in range(n):
  p, name = input().split()
  stu.append([p[8], p[0], i, name])
  
stu.sort(key=lambda x:(x[0],x[1]))

for i in range(n):
  print(stu[i][0]+": "+stu[i][3])
