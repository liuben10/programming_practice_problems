'''
Created on Feb 19, 2016

@author: bliu

? Question 8 In a 2-D matrix, every row is increasingly sorted from left to right, and every column is increasingly sorted from top to bottom. Please implement a function to check whether a number is in such a matrix or not. For example, all rows and columns are increasingly sorted in the following matrix. It returns true if it tries to find number 7, but it returns false if it tries to find number 5.
1 2 8 9
2 4 9 12
4 7 10 13
6 8 11 15

'''


def find_solution_core(matrix, value, row1, col1, row2, col2):
    if (value < matrix[row1][col1] or value > matrix[row2][col2]):
        return False;
    if (value == matrix[row1][col1] or value == matrix[row2][col2]):
        return True
    copyRow1 = row1
    copyRow2 = row2
    copyCol1 = col1
    copyCol2 = col2
    midRow = (row1 + row2) / 2
    midCol = (col1 + col2) / 2
    while midRow != row1 or midCol != col1:
        if (value == matrix[midRow][midCol]):
            return True
        if (value < matrix[midRow][midCol]):
            row2 = midRow
            col2 = midCol
        else:
            row1 = midRow
            col1 = midCol
        midRow = (row1 + row2) / 2
        midCol = (col1 + col2) / 2
    found = False
    if (midRow < len(matrix) - 1):
        found = find_solution_core(matrix, value, midRow+1, copyCol1, copyRow2, midCol)
    if (not found and midCol < len(matrix[0]) - 1):
        found = find_solution_core(matrix, value, copyRow1, midCol + 1, midRow, copyCol2)
    return found

def find_solution(matrix, value):
    rows = len(matrix)
    cols = len(matrix[0])
    return find_solution_core(matrix, value, 0, 0, rows-1, cols-1)

if __name__ == '__main__':
    print find_solution([[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]], 7)


