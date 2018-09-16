class LNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class LNodeBuilder:

    def __init__(self, val):
        self.hp = LNode(val)
        self.tp = self.hp

    def add(self, val):
        if (self.hp is not None):
            self.tp.next = LNode(val)
            self.tp = self.tp.next
        else:
            self.hp = LNode(val)
            self.tp = self.hp
        
def printList(node):
    iter = node
    res = ""
    while (iter is not None):
        res += str(iter.val) + "->"
        iter = iter.next
    print(res)

def removeNFromEnd(hp, n):
    fp = hp
    np = None
    prev = None
    for i in range(n):
        if (fp.next is None):
            raise Exception('Failed to remove N from end due to the input list not being long enough')
        fp = fp.next
    np = hp
    while (fp is not None):
        prev = np
        np = np.next
        fp = fp.next

    prev.next = np.next

    return hp

nodeBuilder = LNodeBuilder(10)

nodeBuilder.add(12)
nodeBuilder.add(13)
nodeBuilder.add(14)

removed = removeNFromEnd(nodeBuilder.hp, 2)
printList(removed)


    


