import statistics
n,m = map(int, input().split())

cnt = 0
cost = 0
for _ in range(n):
  products = list(map(int, input().split()))
  if max(products) - min(products) >= m:
    cnt += 1 
    cost += statistics.mean(products)

print(f"{cnt} {cost}")
