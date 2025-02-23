from collections import Counter

n = int(input())

shoes = list(map(int, input().split()))
cnt = Counter(shoes) #計算每個size出現次數

cos = int(input())
tt = 0

for _ in range(cos):
    s, p = map(int, input().split())
    if cnt[s] > 0:
        tt += p
        cnt[s] -= 1
print(tt)
