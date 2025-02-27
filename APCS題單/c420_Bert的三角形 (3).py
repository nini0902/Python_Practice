n = int(input())

for i in range(1, n+1):
  for j in range(i, n):
    print("_", end = "")
    
  for j in range(1, 2*i):
    print("*", end = "")
    
  for j in range(i, n):
    print("_", end = "")
  print()
