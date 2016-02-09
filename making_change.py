'''
Created on Jan 23, 2016

@author: bliu
'''
import sys

#nondynamic
def making_change(value, coins):
    print "computing=f(" + str(value)+ ")"
    if (value in coins):
        return 1
    else:
        subproblems = []
        for coin in coins:
            if (value - coin >= 0):
                subproblem = making_change(value - coin, coins)
                subproblems.append(subproblem)
        return 1 + min(subproblems)
    
def see_change(solution, value):
    result = []
    while value > 0:
        result.append(solution[value])
        value = value - solution[value]
    return result
    
def making_change_dynamic(value, coins):
    problems = [0] * value
    coin_solutions = [0] * value
    for p in range(1, value):
        min_val = sys.maxint
        min_coin = 0
        for coin in coins:
            if p >= coin:
                if (min_val > 1 + problems[p - coin]):
                    min_val = 1 + problems[p - coin]
                    min_coin = coin
        problems[p] = min_val
        coin_solutions[p] = min_coin
    return problems, coin_solutions
if __name__ == '__main__':
    print see_change(making_change_dynamic(16, [3, 5, 10])[1], 15)
    