n = int(input())

for _ in range(n):
  l1 = list(map(int, input().split()))
  l2 = list(map(int, input().split()))
  wrong = 0
  if l1[1] == l1[3] or l1[1] != l1[5] or l2[1] == l2[3] or l2[1] != l2[5]:
    print("A", end='')
    wrong = 1
  if l1[6] != 1 or l2[6] != 0:
    print("B", end='')
    wrong = 1
  if l1[1] == l2[1] or l1[3] == l2[3] or l1[5] == l2[5]:
    print("C", end='')
    wrong = 1 
  if wrong == 0:
    print("None", end='')
  print()
