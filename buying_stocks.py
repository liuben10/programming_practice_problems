from heap import Heap

'''
can only make one transaction
'''
def max_profit(stock_prices):
    low = 0
    max_profit_so_far = 0
    hi = 0
    while (hi < len(stock_prices)):
        cur_hi = stock_prices[hi]
        if (cur_hi >= stock_prices[low]):
            max_profit_so_far = max(max_profit_so_far, cur_hi - stock_prices[low])
            hi += 1
        else:
            while (low < hi and stock_prices[low] > cur_hi):
                low += 1
    return max_profit_so_far

def profit_comparator(trans1, trans2):
    profit1 = trans1[1] - trans1[0]
    profit2 = trans2[1] - trans2[0]
    if (profit1 > profit2):
        print("t1={} > t2={}".format(trans1, trans2))
    else:
        print("t1={} < t2={}".format(trans1, trans2))
    return profit1 > profit2

def profit(transaction):
    return transaction[1] - transaction[0]

def max_k(stock_prices, k):
    transactions = []
    max_profits = Heap(profit_comparator)
    for i in range(len(stock_prices)):
        max_at_i = (stock_prices[i], stock_prices[i])
        for j in range(i, len(stock_prices)):
            if (profit((stock_prices[i], stock_prices[j])) > profit(max_at_i)):
                max_at_i = (stock_prices[i], stock_prices[j])
        max_profits.push(max_at_i)

    return max_profits.pop_k(k)
    
print(max_profit([2, 1, 5, 4]))
print(max_k([2, 1, 5, 4], 2))
