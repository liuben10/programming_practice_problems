def box_constraint(sudoku, d, row, col):
    boxrow = (row // 3) * 3
    boxcol = (col // 3) * 3
    for r in range(boxrow, boxrow + 3):
        for c in range(boxcol, boxcol + 3):
            if (sudoku[r][c] == d):
                return True
    return False

def constraints(sudoku, domains, row, col):
    filtered_d = []
    for d in domains:
        in_row = True if d in sudoku[row] else False
        in_col = True if d in [sudoku[row][k] for k in range(9)] else False
        in_box = box_constraint(sudoku, d, row, col)
        # print("d=%d, in_row=%s, in_col=%s, in_box=%s" % (d, in_row, in_col, in_box))
        if not (in_row or in_col or in_box):
            filtered_d.append(d)
    return filtered_d

def solve_sudoku(sudoku):
    return solve_sudoku_helper(sudoku)

def solve_sudoku_helper(sudoku):
    domains = [i for i in range(1, 10)]

    for s in sudoku:
        print(s)
    print("\n=========\n")
    
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                constrained = constraints(sudoku, domains, row, col)
                if (not constrained):
                    return None
                didx = 0
                while(sudoku[row][col] == 0 and didx < len(constrained)):
                    sudoku[row][col] = constrained[didx]
                    solved = solve_sudoku_helper(sudoku)
                    if (solved is None):
                        print("Back tracked!")
                        didx += 1
                        sudoku[row][col] = 0
                    else:
                        return solved
                if (didx == len(constrained)):
                    return None
    return sudoku
                
# Solution:
# [5, 3, 4, 6, 7, 8, 9, 1, 2]
# [6, 7, 2, 1, 9, 5, 3, 4, 8]
# [1, 9, 8, 3, 4, 2, 5, 6, 7]
# [8, 5, 9, 1, 6, 7, 4, 2, 3]
# [4, 2, 6, 3, 5, 8, 7, 9, 1]
# [7, 1, 3, 2, 4, 9, 8, 5, 6]
# [9, 6, 1, 5, 3, 7, 2, 8, 4]
# [2, 8, 7, 4, 1, 9, 6, 3, 5]
# [3, 4, 5, 2, 8, 6, 1, 7, 9]
                

# solution = solve_sudoku(
#     [
#         [5, 3, 4, 6, 7, 8, 9, 1, 2],
#         [6, 7, 2, 0, 0, 0, 3, 0, 8],
#         [1, 9, 8, 0, 0, 0, 5, 6, 7],
#         [8, 5, 9, 0, 0, 0, 4, 2, 3],
#         [4, 2, 0, 0, 0, 0, 0, 0, 1],
#         [7, 1, 3, 0, 0, 0, 8, 5, 6],
#         [9, 6, 1, 0, 0, 7, 2, 8, 0],
#         [2, 8, 7, 4, 1, 9, 6, 0, 5],
#         [3, 4, 5, 2, 8, 6, 1, 0, 0],
#     ]
# )

# print("\n Solution: \n")
# for s in solution:
#     print(s)


solution = solve_sudoku(
    [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
)


print("\n Solution: \n")
for s in solution:
    print(s)
