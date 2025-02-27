import sys

while True:
  try:
    n = int(input())
    num = list(map(int, input().split()))
    num = sorted(num, key=lambda x: (x%10, -x))
    print(*num)
  except EOFError:
    break
