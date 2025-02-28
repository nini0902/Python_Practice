import sys 
data = sys.stdin.read().splitlines()
stu = []

for line in data[1:]:
  parts = line.split()
  id = int(parts[0])
  name = parts[1]
  scores = list(map(int, parts[2:]))
  tt_score = sum(scores)
  stu.append([id, name, scores, tt_score])
  
stu.sort(key = lambda x:(-x[3], x[0]))
  
rate = 1
same = 0
last = stu[0][3]
for student in stu:
  if student[3] != last:
    rate += same
    same = 1
    last = student[3]
  elif student[3] == last:
    same += 1 
  print(student[0], student[1], *student[2], student[3], rate)
