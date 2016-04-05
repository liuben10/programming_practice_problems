'''
Created on Apr 3, 2016

@author: bliu
'''


def sumRange(pile, i):
    if (i == 0):
        return 0
    pileSum = 0
    j = 0
    while (j < i and j < len(pile)):
        pileSum += pile[j]
        j += 1
    return pileSum

def takePile(pile, i):
    if (i == 0):
        return ""
    taken = ""
    j = 0
    while (j < i and j < len(pile)):
        taken += "take " +  str(pile[j]) + " from pile=" + str(pile) +"\n"
        j += 1
    return taken


def find_max_pile(piles, N):
    numPiles = len(piles)
    V = [[0] * (N+1) for i in range(numPiles + 1)]
    pileTake = [[""] * (N+1) for i in range(numPiles + 1)]
    for pileIndex in range(1, numPiles+1):
        for i in range(N+1):
            curSum = sumRange(piles[pileIndex-1], i)
            curPileTake = takePile(piles[pileIndex-1], i)
            if (i > len(piles[pileIndex-1])):
                curSum += V[pileIndex-1][i-len(piles[pileIndex-1])]
                curPileTake += pileTake[pileIndex-1][i-len(piles[pileIndex-1])]
            if (curSum >= V[pileIndex-1][i]):
                V[pileIndex][i] = curSum
                pileTake[pileIndex][i] = curPileTake
            else:
                V[pileIndex][i] = V[pileIndex-1][i]
                pileTake[pileIndex][i] = pileTake[pileIndex-1][i]
    print pileTake[pileIndex][i]
    return V
    
if __name__ == '__main__':
    #print find_max_pile([[2, 8, 3], [4, 5, 6], [2, 3, 4], [1, 2, 100]], 4)
    #print find_max_pile([[1, 2], [3, 4], [5, 6], [8, 100]], 4)
    print find_max_pile([[1, 2]], 3)