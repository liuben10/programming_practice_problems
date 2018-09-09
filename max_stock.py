def max_stock(stocks):
    if (len(stocks) <= 1):
        return 0
    slow_p = 0
    high_p = 1
    maxProfit = 0
    profit_so_far = 0
    while (high_p < len(stocks)):
        if (stocks[high_p] > stocks[slow_p] or slow_p == high_p):
            profit_so_far = stocks[high_p] - stocks[slow_p]
            if (profit_so_far > maxProfit):
                maxProfit = profit_so_far
            high_p += 1
        else:
            profit_so_far = stocks[high_p] - stocks[slow_p]
            if (profit_so_far > maxProfit):
                maxProfit = profit_so_far
            slow_p += 1
    return maxProfit
    


print(max_stock([5, 4, 9, 10, 2, 3]))
print(max_stock([1,2,3,4,5,6,7,8]))
print(max_stock([4, 5, 9, 10, 2, 11]))
