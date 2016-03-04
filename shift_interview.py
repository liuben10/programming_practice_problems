'''
Created on Mar 2, 2016

@author: bliu
'''

def inTuple(tuple, element):
    return element >= tuple[0] and element <= tuple[1]


def merge(srcTuple, destTuple, pair):
    if (srcTuple is None and destTuple is None):
        return pair
    if (srcTuple == destTuple):
        return srcTuple
    if (destTuple is None and pair[1] > srcTuple[1]):
        return [srcTuple[0], pair[1]]
    if (srcTuple is None and pair[0] < destTuple[0]):
        return [pair[0], destTuple[1]]
    return [srcTuple[0], destTuple[1]]


def subsumed(tuple, mergedTuple):
    return tuple[0] >= mergedTuple[0] and tuple[1] <= mergedTuple[1]


def merge_pair(pairs, pair):
    if (len(pairs) == 0):
        return None
    srcTuple = None
    destTuple = None
    for tuple in pairs:
        if inTuple(tuple, pair[0]):
            srcTuple = tuple
        if inTuple(tuple, pair[1]):
            destTuple = tuple
    mergedTuple = merge(srcTuple, destTuple, pair)
    result = []
    mergedAlready = False
    for tuple in pairs:
        if tuple == srcTuple or tuple == destTuple or subsumed(tuple, mergedTuple):
            continue
        if (tuple[0] > mergedTuple[1] and not mergedAlready):
            result.append(mergedTuple)
            mergedAlready = True
        result.append(tuple)
    if (not mergedAlready):
        result.append(mergedTuple)
    return result


if __name__ == '__main__':
    print merge_pair([[0,3], [6,10],[13,15]], [2, 7])
    print merge_pair([[0,3], [6,10],[13,15]], [2, 14])
    print merge_pair([[0,3], [6,10],[13,15]], [7, 14])
    print merge_pair([[0,3], [6,10],[13,15]], [2, 5])
    print merge_pair([[0,3], [6,10],[13,15]], [-1, 3])
    print merge_pair([[0,3], [6,10],[13,15]], [-1, 5])
    print merge_pair([[0,3], [6,10],[13,15]], [4, 5])
    print merge_pair([[0,3], [6,10],[13,15]], [7, 9])
    print merge_pair([[0,3], [6,10],[13,15]], [-1000, -900])
    print merge_pair([[0,3], [6,10],[13,15]], [900, 1000])

