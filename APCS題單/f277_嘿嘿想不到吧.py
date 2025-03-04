n = int(input())
stu = []

for line in range(n):
  p = list(map(str, input().split()))
  name = p[0]
  c = int(p[1])
  num = int(p[2])
  sen = p[3]
  stu.append([c, num, name, sen])
  
stu.sort(key = lambda x:(x[0], x[1]))

for i in range(n):
  print(*stu[i][:3])
  print(stu[i][3])
