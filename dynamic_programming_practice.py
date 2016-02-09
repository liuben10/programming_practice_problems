'''
Created on Jan 31, 2016

@author: bliu
'''
import sys

'''
Knapsack problem definition:
inputs:

values = value of each item. NOTE: with these inputs there is a requirement that values and weights contain
0 starting at the beginning.  This is because i goes from 1 to n+1 so the 0th value must be defined as 0 to be
able to factor in the first element for knapsack.

That is if values = [1, 2, 3, 4] and n = 4, then we must transform values to be [0, 1, 2, 3,4]

weight = weight of each item.
n = number of items.  
W = maximum weight.
Knapsack: 
Subproblem definition: In Knapsack, the subproblems are defined as the V[i, w] where i = all pieces up to the
ith piece and w is the weight up to w.  This is means we are going to be solving it piece by piece, starting with
the optimal solution to the first piece, first and second, etc.

subproblems are initialized in V.  The V[i, w] subproblem can be retrieved through this method
Either we keep the item (using the value V[i-1][w]), or we take the item calculated by
V[i-1][w-weight[i]] + v[i] if this value is more valuable than the value V[i-1][w].  If we ever take the
value V[i-1][w-weight[i]] + v[i], then that means we are taking the item so if we keep the 2d array keep, then
we must indicate the item is kept.
'''
def knapsack_problem(values, weights, W):
    n = len(values)
    values.insert(0, 0)
    weights.insert(0, 0)
    V = [[0] * (W+1) for i in range(n+1)]
    keep = [[0] * (W+1) for i in range(n+1)]
    for i in range(1, n+1):
        for w in range(W+1):
            if weights[i] <= w and values[i] + V[i-1][w-weights[i]] > V[i-1][w]:
                V[i][w] = values[i] + V[i-1][w-weights[i]]
                keep[i][w] = 1
            else:
                V[i][w] = V[i-1][w]
                keep[i][w] = 0
    K = W
    for i in range(n, 0, -1):
        if (keep[i][K] == 1):
            print "keeping= " + str(values[i])
            K = K - weights[i]
    return V

'''
In edit distance, we are attempting to minimize the amount of edits needed to transform
word_a  into word_b.

The possible operations are:

insertion: insert a letter in word_a.
deletion: delete a letter in word_a.
substitution: replace a letter in word_a with a letter not equal to that letter.

subproblems:
to find the maximum edit distance of word_a, and word_b, it suffices to find the maximum edit distance
for the xth word (x iterates through the length of word_a), and the yth word (y iterates through the length of word_b).
Therefore, for sanctuary and sarcastic.

The subproblems start off as 0, 0 for no letters. and we will end up solving the edit distance for
sanctuary and ' ', sanctuary and s, sarcas and sanct etc.

To initialize, the first step is to initialize everything in the first column and the first row to the values of their index
since the solution to those is just the length of the word.

Suppose our subproblems are stored as S.  We must determine how the updates will be carried out.
So to solve for S[x][y] = min { insert, delete, substitution} or no_op.  delete = S[x-1][y]+1, insert = S[x][y-1] + 1
Substitution = S[x-1][y-1] + 1 or no_op = S[x-1][y-1]

'''
def edit_distance(word_a, word_b):
    m = len(word_a)
    n = len(word_b)
    sub_problems = [[0] * n for i in range(m)]
    operation = [[""] * n for i in range(m)]
    for i in range(1, m):
        sub_problems[i][0] = i
    for j in range(1, n):
        sub_problems[0][j] = j
    for x in range(m):
        for y in range(n):
            if word_a[x] == word_b[y]:
                sub_problems[x][y] = sub_problems[x-1][y-1]
            else:
                insert = sub_problems[x-1][y] + 1
                delete = sub_problems[x][y-1] + 1
                substitution = sub_problems[x-1][y-1] + 1
                
                min_val = min(insert, delete, substitution)
                if (min_val == insert):
                    operation[x][y] = "insert"
                elif (min_val == delete):
                    operation[x][y] = "delete"
                else:
                    operation[x][y] = "substitution"
                sub_problems[x][y] = min_val
    
    print_2d_array_nice(operation)
    print_2d_array_nice(sub_problems)
            
    
            
def print_2d_array_nice(matrix):
    for row in matrix:
        print str(row) + "\n"

def make_change(coins, value):
    sub_problems = [0] * value
    coin_solution = [0] * value
    for p in range(1, value):
        min_val = sys.maxint
        coin = 0
        for w in coins:
            if (p >= w):
                if (1 + sub_problems[p-w] < min_val):
                    min_val = 1 + sub_problems[p-w]
                    coin = w
            sub_problems[p] = min_val
            coin_solution[p] = coin
    print sub_problems
    print coin_solution
    j = value-1
    coins = []
    while j > 0:
        coins.append(coin_solution[j])
        j = j - coin_solution[j]
    print coins
    
if __name__ == '__main__':
    knapsack_problem([3, 4, 2], [2, 5, 4], 10)