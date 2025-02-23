from collections import defaultdict

n, m = map(int, input().split())

#建立 defaultdict 儲存A的位置索引
A = defaultdict(list)

for i in range(1, n+1):
    word = input()
    A[word].append(i) #索引
    
for _ in range(m):
    word = input()
    if word in A:
        print(" ".join(map(str, A[word])))
    else: print("-1")
