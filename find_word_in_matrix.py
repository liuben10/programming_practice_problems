'''
Created on Jan 23, 2016

@author: bliu
'''
from __builtin__ import False

def contains(visited, coordinate):
    for e in visited:
        if e[0] == coordinate[0] and e[1] == coordinate[1]:
            return True
    return False


def has_path_core(input, x, y, path):
    visited = []
    for i in range(len(input)):
        visited.append([0] * len(input[0]))
    stack = []
    stack.append([x, y])
    pathsofar = input[y][x]
    visited[y][x] = 1
    while(stack):
        successors = []
        current_coordinate = stack.pop()
        cury = current_coordinate[1]
        curx = current_coordinate[0]
        if (cury + 1 < len(input)):
            successors.append([curx, cury+1])
        if (curx + 1 < len(input[cury])):
            successors.append([curx+1, cury])
        if (cury - 1 >= 0):
            successors.append([curx, cury-1])
        if (curx - 1 >= 0):
            successors.append([curx-1, cury])
        for successor in successors:
            if (visited[successor[1]][successor[0]] != 1):
                if (input[successor[1]][successor[0]] == path[len(pathsofar)]):
                    stack.append(current_coordinate)
                    stack.append(successor)
                    visited[successor[1]][successor[0]] = 1
                    pathsofar += input[successor[1]][successor[0]]
                    current_coordinate = successor
                    if pathsofar == path:
                        return True
        if (current_coordinate[0] == curx and current_coordinate[1] == cury):
            if (len(stack) == 0):
                break
            stack.pop()
    return False

def has_path(input, path):
    for y in range(len(input)):
        for x in range(len(input[y])):
            if (has_path_core(input, x, y, path)):
                return True
    return False
    
    
if __name__ == '__main__':
    print has_path([["a", "b", "d"], ["b", "b", "b"], ["c", "b", "f"]], "abbc")
        
    