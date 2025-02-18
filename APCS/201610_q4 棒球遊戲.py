while True:
  try:
    dic = {}
    for i in range(9):
      l = input().split()
      dic[i] = l[1:]
    target = int(input())
    out = 0
    b1 = 0
    b2 = 0
    b3 = 0
    b4 = 0
    score = 0
    player = -1
    while True:
      run_base = 0 # 待會要跑幾壘
      player = (player+1)%9 # 選手輪轉
      hit = dic[player].pop(0) #取得該次打擊資訊
      if hit == "SO" or hit == "FO" or hit == "GO":
        out += 1 
        if out == target:
          break
        # 三出局(清空壘包)
        if out%3 == 0:
          b1 = 0
          b2 = 0
          b3 = 0
          b4 = 0
      elif hit == "HR":
        run_base = 4
      else:
        run_base = int(hit[0])
      b4 = 1
      for j in range(run_base):
        b1,b2,b3,b4 = b2,b3,b4,b1
        if b4 == 1: # 有人回本壘
          score += 1 
          b4 = 0
    print(score)
  except:
    break
