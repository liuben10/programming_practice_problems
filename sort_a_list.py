'''
Created on Feb 20, 2016

@author: bliu
'''

class Node:
    def __init__(self, value, next):  # @ReservedAssignment
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
    beforeFringe = aList
    fringePtr = aList.next
    head = Node(None, aList)
    while (fringePtr is not None):
        findInPlacePtr = head.next    
        prevPtr = head
        while ( findInPlacePtr is not fringePtr):
            if (fringePtr.value <= findInPlacePtr.value):
                tmpPtr = fringePtr.next
                fringePtr.next = findInPlacePtr
                beforeFringe.next = tmpPtr
                prevPtr.next = fringePtr
                fringePtr = tmpPtr
                break
            else:
                prevPtr = findInPlacePtr
                findInPlacePtr = findInPlacePtr.next
        fringePtr = fringePtr.next
        beforeFringe = fringePtr.next
    return head.next
                
            
        
def printAList(aList):
    iter = aList  # @ReservedAssignment
    while (iter is not None):
        print iter.value
        iter = iter.next  # @ReservedAssignment
        
if __name__ == '__main__':
    c = Node(4, None)
    d = Node(12, c)
    b = Node(13, d)
    a = Node(15, b)
    x = Node(7, a)
    sortAList(x)
    printAList(x)
        