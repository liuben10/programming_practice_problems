def jump_solution(jumps):
    fringe = []
    fringe.append((0, 0))
    pathSoFar = []
    idx = 0
    while (fringe):
        head = fringe.pop()
        idx = head[0]
        numjumps = head[1]
        if (idx == len(jumps) - 1):
            return numjumps
        for i in range(jumps[idx], 0, -1):
            fringe.insert(0, (i + idx, numjumps + 1))
    return -1
                

print(jump_solution([2,3,1,1,4]))
        
        
