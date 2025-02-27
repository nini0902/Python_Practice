s = list(input())

last = ord(s[0])
for i in range(1, len(s)):
  print(abs(ord(s[i]) - last), end = "")
  last = ord(s[i])
