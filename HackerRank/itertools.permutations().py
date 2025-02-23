from itertools import permutations

string, n = input().split()
n = int(n)

#把每個組合轉成字串並用list儲存
result = [''.join(i) for i in permutations(sorted(string), n)]

result.sort() #排序

for i in result: print(i)
