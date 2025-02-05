a,b,result = map(int, input().split())

if a > 1: a = 1
if b > 1: b = 1

if a & b == result: print("AND") 
if a | b == result: print("OR")
if a ^ b == result: print("XOR")

if a&b!=result and a|b!=result and a^b!=result:
  print("IMPOSSIBLE")
