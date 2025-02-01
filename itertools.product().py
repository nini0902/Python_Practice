from itertools import product 
A = list(map(int, input().split()))
B = list(map(int, input().split()))

#返回的是迭代器，並無產生完整列表(延遲計算)
result = product(A,B)

#利用迴圈才真正計算並產生組合
for pair in result:
    print(pair, end = " ")
