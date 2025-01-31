if __name__ == '__main__':
    N = int(input())
    L = []
    i = None
    e = None

    for _ in range(N):
        part = input().split()
        instr = part[0]
        
        if instr == "insert":
            i = int(part[1])
            e = int(part[2])
            L.insert(i, e)
        elif instr == "remove":
            e = int(part[1])
            if e in L: L.remove(e)
        elif instr == "append":
            e = int(part[1])
            L.append(e)
        elif instr == "pop":
            if L: L.pop()
        elif instr == "reverse":
            L.reverse()
        elif instr == "sort":
            L.sort()
        elif instr == "print":
            print(L)
