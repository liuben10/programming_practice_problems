'''
Created on Feb 20, 2016

@author: bliu
'''

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


def swap(prevPtr, initPtr):
    tmpPtr = initPtr.next
    initPtr.next = prevPtr
    prevPtr.next = tmpPtr
    
def getSize(aList):
    size = 0
    initPtr = aList
    while (initPtr is not None):
        initPtr = initPtr.next
        size += 1
    return size


def sortAList(aList):
    if (aList.next is None or aList is None):
        return aList
    
    fringePtr = aList.next
    head = Node(None, aList)
    while (fringePtr is not None):
        findInPlacePtr = head.next    
        prevPtr = head
        while ( findInPlacePtr is not fringePtr):
            if (fringePtr.value <= findInPlacePtr.value):
                tmpPtr = fringePtr.next
                fringePtr.next = findInPlacePtr
                findInPlacePtr.next = tmpPtr
                prevPtr.next = fringePtr
                break
            else:
                prevPtr = findInPlacePtr
                findInPlacePtr = findInPlacePtr.next
        fringePtr = fringePtr.next
    return head.next
                
            
        
def printAList(aList):
    iter = aList
    while (iter is not None):
        print iter.value
        iter = iter.next
        
if __name__ == '__main__':
    c = Node(4, None)
    b = Node(5, c)
    a = Node(3, b)
    sortAList(a)
    printAList(a)
        