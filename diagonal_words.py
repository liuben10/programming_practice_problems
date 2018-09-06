def zigzagged_words(input_str, num_rows):
    if (num_rows == 1 or len(input_str) == 1):
        return input_str
    rows = [[] for i in range(num_rows)]
    ridx = 0
    for c in input_str[1:]:
        if (((ridx) // (num_rows-1)) % 2):          
            rows[num_rows - (ridx % (num_rows-1)) - 2].append(c)
        else:
            rows[((ridx) % (num_rows-1)) + 1].append(c)
        ridx += 1
    res = input_str[0]
    print(rows)
    for row in rows:
        res += "".join(row)
    return res
    
print(zigzagged_words("PAYPALISHIRING", 3))
print(zigzagged_words("PAYPALISHIRING", 4))
