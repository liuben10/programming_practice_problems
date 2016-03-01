'''
Created on Feb 20, 2016

@author: bliu
'''


class LinkedListNode:
    def __init__(self, value, next):
        self.value = value
        self.next = next

 
         
def find_kth_from_end(aList, k):
    fastPtr = aList
    slowPtr = aList
    cnt = 0
    while (fastPtr is not None and cnt != k):
        fastPtr = fastPtr.next
        cnt += 1
    if fastPtr is None:
        if cnt == k:
            return slowPtr.value
        else:
            return None
    while fastPtr is not None:
        fastPtr = fastPtr.next
        slowPtr = slowPtr.next
    return slowPtr.value

if __name__ == '__main__':
    c = LinkedListNode(3, None)
    b = LinkedListNode(4, c)
    a = LinkedListNode(5, b)
    d = LinkedListNode(6, a)
    print find_kth_from_end(d, 2)
    
   
    