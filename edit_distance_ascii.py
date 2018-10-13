def ascii_deletion_distance(str1, str2):
    N = len(str1)
    M = len(str2)
    table = [[0 for c in range(N + 1)] for j in range(M + 1)]
    for i in range(1, N+1):
        table[0][i] = ord(str1[i-1])
    for j in range(1, M+1):
        table[j][0] = ord(str2[j-1])

    for i in range(1, N+1):
        for j in range(1, M+1):
            if (str2[j-1] == str1[i-1]):
                table[j][i] = table[j-1][i-1]
            else:
                addition = table[j-1][i] + ord(str2[j-1])
                subtraction = table[j][i-1] + ord(str1[i-1])
                replace = table[j-1][i-1] + ord(str1[i-1]) + ord(str2[j-1])
                table[j][i] = min(addition, replace, subtraction)
    for r in table:
        print(r)
    return table[M][N]

print(ascii_deletion_distance("cat", "at"))
