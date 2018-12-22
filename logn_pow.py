def logn_pow(x, n):
    if (n == 1):
        return x
    elif (n < 0):
        return 1 / logn_pow(x, abs(n))
    elif n % 2:  
        return x * logn_pow(x, n-1)
    else:
        half_pow = logn_pow(x, n/2)
        return half_pow * half_pow

print(logn_pow(4, -2))
