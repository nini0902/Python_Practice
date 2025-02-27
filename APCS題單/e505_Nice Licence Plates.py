n = int(input())
for _ in range(n):
  s = list(input())
  
  cnt1 = cnt2 = 0
  
  cnt1 += (ord(s[0]) - ord("A")) * (26**2)
  cnt1 += (ord(s[1]) - ord("A")) * (26**1)
  cnt1 += (ord(s[2]) - ord("A")) * (26**0)
  
  cnt2 += int(s[4])*1000 + int(s[5])*100 + int(s[6])*10 + int(s[7])
  
  if abs(cnt1 - cnt2) <= 100: 
    print("nice")
  else:
    print("not nice")
