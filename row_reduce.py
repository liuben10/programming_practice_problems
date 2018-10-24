
def swap_two_rows(matrix, i1, i2):
    tmp = matrix[i1]
    matrix[i1] = matrix[i2]
    matrix[i2] = tmp

def add_two_rows(row1, row2):
    for i in range(len(row1)):
        row1[i] = row1[i] + row2[i]
    return row1
    
def multiply_row(row, scalar):
    return list(map(lambda x: x * scalar, row))

def gcd(larger, smaller):
    # print("gcd %s, %s" % (larger, smaller))
    if (larger == smaller):
        return smaller
    else:
        new_larger = max(larger-smaller, smaller)
        new_smaller = min(larger-smaller, smaller)
        return gcd(new_larger, new_smaller)

def lcm(x, y):
    x1 = abs(x)
    x2 = abs(y)
    larger = max(x1, x2)
    smaller = min(x1, x2)
    the_gcd = gcd(larger, smaller)
    return (x1 * x2) // the_gcd

def find_first_row_to_swap(matrix, i, cidx):
    rows = len(matrix)
    for j in range(i, rows):
        row = matrix[j]
        new_lead = row[cidx]
        if (new_lead != 0):
            return (new_lead, j)
    return -1, -1

def find_scale(row):
    for el in row:
        if (el != 0):
            return abs(el)
    return 0

def rref(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    cidx = 0
    for i in range(rows):
        if (cidx >= cols):
            break
        row = matrix[i]
        leading = row[cidx]

        if (leading == 0):
            new_lead, swap_idx = find_first_row_to_swap(matrix, i, cidx)
            if (swap_idx != -1):
                swap_two_rows(matrix, swap_idx, i)
                leading = new_lead
        if (leading is not 0):
            for j in range(rows):
                if (j is not i):
                    other_row = matrix[j]
                    lead_at_j = other_row[cidx]
                    if (lead_at_j is not 0):
                        _lcm = lcm(lead_at_j, leading)
                    
                        leading_factor = _lcm // leading
                        other_leading_factor = _lcm // lead_at_j
                    
                        scaled = multiply_row(row, -leading_factor)
                        
                        other_scaled = multiply_row(other_row, other_leading_factor)
                        
                        added = add_two_rows(scaled, other_scaled)

                        matrix[j] = added
        cidx += 1

    for i, r in enumerate(matrix):
        scale = find_scale(r)
        if (scale != 0):        
            reduced = multiply_row(r, 1 / scale)
            matrix[i] = reduced
    return matrix



def test_case(input_m):
    print("\n----------\n")
    print("====Input====")
    for r in input_m:
        print(r)
    print("=============")
    reduced = rref(input_m)
    print("====Output===")
    for r in reduced:
        print(r)
    print("=============")


testm = [
    [5, 12, 9],
    [12, 13, 16],
    [4, 9, 12]
]

test_case(testm)
        
testm = [
    [5, 12, 14],
    [8, 12, 116],
    [13, 3, 3],
    [2, 5, 9]
]

test_case(testm)

testm = [
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3]
]

test_case(testm)


testm = [
    [5, 2, 3],
    [2, 3, 1]
]

test_case(testm)
