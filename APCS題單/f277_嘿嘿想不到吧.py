n = int(input())
stu = []

for line in range(n):
  p = input().split()
  c, num = int(p[1]), int(p[2])
  stu.append([c, num, p[0], p[3]])
  
stu.sort()

for i in range(n):
  print(*stu[i][:3])
  print(stu[i][3])
