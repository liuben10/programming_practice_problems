"""
https://leetcode.com/problems/combinations/description/
"""
def combinations(n, k):
    if (n == 0):
        return []
    if (k == 1):
        return [[i] for i in range(1, n+1)]
    res = {}
    for i in range(1,n+1):
        combos = combinations(n, k-1)
        for c in combos:
            combined = [i] + c
            
            res[tuple(sorted(combined))] = 1

    joined = [list(k) for k in res.keys()]
    return joined
        


print(combinations(4,2))
