'''
Created on Apr 4, 2016

@author: bliu
'''

def order_equality(astr, bstr):
    aOrderMap = getOrderMap(astr)
    bOrderMap = getOrderMap(bstr)
    return convToSet(aOrderMap) == convToSet(bOrderMap)

def convToSet(aMap):
    resSet = set()
    aMap.update((k, frozenset(v)) for k, v in aMap.iteritems())
    for key in aMap:
        resSet.add(aMap[key])
    return resSet

def getOrderMap(aStr):
    orderMap = {}
    index = 0
    for c in aStr:
        if c in orderMap:
            orderMap[c].add(index)
        else:
            orderMap[c] = set([index])
        index += 1
    return orderMap