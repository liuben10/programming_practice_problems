from functools import reduce

def product_of_everything_except_itself(input_arr):
    product = reduce(lambda x, y: x * y, input_arr)
    output = [0 for i in range(len(input_arr))]
    return list(map(lambda x: product // x, input_arr))

# also needs to be O(n)
def product_of_everything_except_itself_wo_div(input_arr):
    lwindows = [1 for i in range(len(input_arr))]
    rwindows = [1 for i in range(len(input_arr))]
    for i in range(len(input_arr)-1, -1, -1):
        if ( i + 1 < len(input_arr)):
            rwindows[i] = input_arr[i+1] * rwindows[i+1]

    for i in range(len(input_arr)):
        if (i-1 >= 0):
            lwindows[i] = input_arr[i-1] * lwindows[i-1]

    output = [lwindows[i] * rwindows[i] for i in range(len(input_arr))]
    return output
    
    
output = product_of_everything_except_itself_wo_div([14, 13, 26, 28])
print(output)
