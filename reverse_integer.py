def reverse_integer(n):
    nrev = 0
    while (n > 0):
        dig = n % 10
        nrev = (nrev * 10) + dig
        n = n // 10
    return nrev

print(reverse_integer(245))
        
