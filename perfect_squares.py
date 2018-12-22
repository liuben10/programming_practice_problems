def is_perfect_square(apositiveint):
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True
        
def perfect_squares(n):
    if (is_perfect_square(n)):
        return 1
    else:
        squared_subproblems = []
        for i in range(1, n):
            if (i <= 1 or is_perfect_square(i)):
                squared_subproblems.append(perfect_squares(n-i))
        return min(squared_subproblems) + 1

def perfect_squares_dp(n):
    table = [0 for i in range(n+1)]
    squares = []
    for i in range(1, n+1):
        prod = i*i
        if (prod <= n):
            table[prod] = 1
            squares.append(prod)
    if (table[n] == 1):
        return 1
    for i in range(1, n+1):
        if (table[i] != 1):
            subproblems = []
            for j in squares:
                if (i-j > 0):
                    subproblems.append(table[i-j])
            table[i] = min(subproblems) + 1
    return table[n]
                    
   
    
print(perfect_squares_dp(12))
