def edit_distance(s1, s2):
    table = [[0 for i in range(len(s1) + 1)] for j in range(len(s2) + 1)]
    for i in range(len(s1)+1):
        table[0][i] = i
    for i in range(len(s2) + 1):
        table[i][0] = i

    for s1p in range(1, len(s1) + 1):
        for s2p in range(1, len(s2) + 1):
            if (s1[s1p-1] == s2[s2p-1]):
                table[s2p][s1p] = table[s2p-1][s1p-1]
            else:
                table[s2p][s1p] = min(
                    table[s2p-1][s1p] + 1,
                    table[s2p][s1p-1] + 1,
                    table[s2p-1][s1p-1] + 1,
                )

    for r in table:
        print(r)
    return table[len(s2)][len(s1)]

print(edit_distance("phil", "pyirk"))
