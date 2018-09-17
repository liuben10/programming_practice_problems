def spiral_matrix_generator(n):
    nums_to_ingest = list(range(1, pow(n, 2)+1))

    res = [[0 for i in range(n)] for j in range(n)]

    direction = 0
    row=0
    col=0
    while(nums_to_ingest):
        elem = nums_to_ingest.pop(0)
        res[row][col] = elem
        if (direction == 0):
            if (col + 1 < n and res[row][col+1] == 0):
                col += 1
            else:
                direction = (direction + 1) % 4
                row += 1
        elif direction == 1:
            if row + 1 < n and res[row+1][col] == 0:
                row += 1
            else:
                direction = (direction + 1) % 4
                col -= 1
        elif direction == 2:
            if col - 1 >= 0 and res[row][col-1] == 0:
                col -= 1
            else:
                direction = (direction + 1) % 4
                row -= 1
        elif direction == 3:
            if row - 1 >= 0 and res[row-1][col] == 0:
                row -= 1
            else:
                direction = (direction + 1) % 4
                col += 1
    return res

print(spiral_matrix_generator(4))
