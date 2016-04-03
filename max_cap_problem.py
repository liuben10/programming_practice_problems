'''
Created on Mar 12, 2016

@author: bliu
'''



def getMaxCap(expenditures, budget):
    maxSoFar = []
    if (len(expenditures) > budget):
        return 0
    if (len(expenditures) == budget):
        return 1
    expenditures.sort()
    for i in range(budget+1):
        maxSoFar.append(0)
    uncapIndex = 0
    maxCapSoFar = 0
    for i in range(1, budget+1):
        nextMaxCap = maxCapSoFar + 1
        nextMaxSum = 0
        curMax = maxSoFar[i-1]
        while uncapIndex < len(expenditures) and expenditures[uncapIndex] <= nextMaxCap:
            cur = expenditures[uncapIndex]
            if (cur <= nextMaxCap):
                nextMaxSum += cur
                uncapIndex += 1
        newCaps = nextMaxCap * (len(expenditures) - uncapIndex)
        nextMaxSum += newCaps
        if nextMaxSum > budget:
            maxSoFar[i] = maxSoFar[i-1]
        else:
            maxSoFar[i] = nextMaxSum
            maxCapSoFar = nextMaxCap
    return maxSoFar[budget]

if __name__ == '__main__':
    print getMaxCap([3, 2, 5], 6)
    
    