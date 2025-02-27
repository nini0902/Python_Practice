n = int(input())
num1 = map(int, input().split())
num1 = sorted(num1)
print(*num1)
num = set(num1)

num = sorted(num, reverse = True)
print(*num)
