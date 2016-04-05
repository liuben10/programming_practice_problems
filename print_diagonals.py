'''
Created on Apr 4, 2016

@author: bliu
'''


def print_diagonal(aMatrix, row, col, rows, cols):
    resString = ""
    for i, j in zip(range(row, rows), range(col, cols)):
        resString += str(aMatrix[i][j]) + " "
    print resString


def print_lower(aMatrix, rows, cols):
    for i in range(rows):
        print_diagonal(aMatrix, i, 0, rows, cols)


def print_upper(aMatrix, rows, cols):
    for i in range(1, cols):
        print_diagonal(aMatrix, 0, i, rows, cols)


def printDiagonals(aMatrix):
    rows = len(aMatrix)
    cols = len(aMatrix[0])
    print_lower(aMatrix, rows, cols)
    print_upper(aMatrix, rows, cols)
    
if __name__ == '__main__':
    testMatrix = [
        [1, 2, 3],
        [3, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]
    printDiagonals(testMatrix)