
l = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        l.append((name, score))
        
    l.sort(key=lambda x : x[1])
    
    lowest = l[0][1]
    second_low = None
    
    for name, score in l:
        if(score > lowest):
            second_low = score
            break
            
    second_low_stu = [name for name, score in l if score == second_low]
    
    second_low_stu.sort()
    
    for name in second_low_stu:
        print(name)
