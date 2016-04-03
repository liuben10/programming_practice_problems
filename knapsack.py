'''
Created on Apr 3, 2016

@author: bliu
'''


def knapsack(values, weights, N, W):
    V = [[0] * (W+1) for i in range(N+1)]
    for i in range(1, N+1):
        for w in range(W+1):
                if (weights[i-1] <= w):
                    V[i][w] = max([V[i-1][w], values[i-1] + V[i][w-weights[i-1]]])
                else:
                    V[i][w] = V[i-1][w]
    return V
    
if __name__ == '__main__':
    print knapsack([3, 4, 5], [5, 6, 8], 3, 12)