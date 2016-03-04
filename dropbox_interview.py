'''
Created on Mar 3, 2016

@author: bliu

Dropbox interview question. Find set of all subsets of an array of prices that will sum to a target value.

inputs:
prices = array of prices.
budget = allowed budget that the subsets must sum to.

output = set of all lists that sum to a particular budget.
'''

def find_combinations(prices, budget):
    subproblems = []
    for i in range(budget+1):
        subproblems.append(set())
    for i in range (1, budget+1):
        for price in prices:
            if (price == i):
                curtup = (price,)
                subproblems[i].add(curtup)
            elif(price < i):
                previous = subproblems[i-price]
                for j in previous:
                    jlist = list(j)
                    jlist.append(price)
                    jlist.sort()
                    jtup = tuple(jlist)
                    subproblems[i].add(jtup)
    return subproblems[budget]

if __name__ == '__main__':
    print find_combinations([1, 2, 3, 5], 6)