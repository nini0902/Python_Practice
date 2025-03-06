def can_rearrange(N, l):
    now = 1
    stack = []
    
    for t in l:
      while now <= N and(not stack or stack[-1] != t):
        # 當前車廂不符合順序或是 stack 為空就把車推進來
        stack.append(now)
        now += 1 
      if stack and stack[-1] == t: # 如果當前車站最上面的車符合就出站
        stack.pop()
      else:
        return "No"
    return "Yes"
  
while True:
  N = int(input())
  if N == 0: break
  while True:
    train = list(map(int, input().split()))
    if train == [0]: break
    print(can_rearrange(N, train))
