def determine_sign(res, dividend, divisor):
    if ((dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0)):
        return res
    else:
        return -1 * res
    

def division(dividend, divisor):
    res = 0
    absolute_div = abs(divisor)
    div_copy = dividend
    while(div_copy > 0):
        res += 1
        div_copy -= absolute_div

    return determine_sign(res, dividend, divisor)

print(division(100, 4))
