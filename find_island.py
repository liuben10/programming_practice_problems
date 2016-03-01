


def dfs(aMatrix, row, col, visited):
    fringe = []
    fringe.append([row, col])
    while (fringe):
        visiting = fringe.pop()
        visited.append(visiting)
        curcol = visiting[1]
        currow = visiting[0]
        successors = []
        if (curcol + 1 < len(aMatrix)):
            successors.append([currow, curcol+1])
        if (currow + 1 < len(aMatrix[curcol])):
            successors.append([currow+1, curcol])
        if (curcol - 1 >= 0):
            successors.append([currow, curcol-1])
        if (currow - 1 >= 0):
            successors.append([currow-1, curcol])
        for successor in successors:
            if successor not in visited and successor not in fringe and aMatrix[successor[0]][successor[1]] == 'x':
                fringe.append(successor)


def find_islands(aMatrix):
    visited = []
    islands = 0
    rows = len(aMatrix)
    for row in range(rows):
        currow = aMatrix[row]
        for col in (range(len(currow))):
            if (aMatrix[row][col] == 'x' and not [row, col] in visited):
                islands += 1
                dfs(aMatrix, row, col, visited)
    return islands
    
if __name__ == '__main__':
    test_in = [[' ', ' ', 'x'],
               ['x', ' ', ' '], 
               ['x', ' ', 'x']]
    print find_islands(test_in)