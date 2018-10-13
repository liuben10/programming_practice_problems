def find_max_matrix(testIn):
    matrix_of_maxes = [[0 for i in range(len(testIn))] for j in range(len(testIn))]
    for i in range(len(testIn)):
        matrix_of_maxes[i][i] = testIn[i]
        for j in range(i):
            matrix_of_maxes[i][j] = max(matrix_of_maxes[i-1][j], testIn[i])
    return matrix_of_maxes




max_matrices = find_max_matrix([5, 9, 10, 12, 3, 2, 4, 9, 15, 19, 8, 16])
for r in max_matrices:
    print(r)


