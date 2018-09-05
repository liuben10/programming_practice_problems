class ListBuilder:
    def __init__(self):
        self.hp = None
        self.tp = None

    def append(self, x):
        if (self.hp == None):
            self.hp = ListNode(x)
            self.tp = self.hp
        else:
            self.tp.next = ListNode(x)
            self.tp = self.tp.next
        return self

    def build(self):
        return self.hp

    def clear(self):
        self.hp = None
        self.tp = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        


def addTwoNumbers(l1, l2):
    summed = None
    hp = None
    i1 = l1
    i2 = l2
    carry = 0
    digSum = 0
    while(i1 != None and i2 != None):
        digSum = carry + i1.val + i2.val
        addMe = digSum % 10
        carry = digSum // 10
        if (summed == None):
            summed = ListNode(addMe)
            hp = summed
        else:
            summed.next = ListNode(addMe)
            summed = summed.next
        i1 = i1.next
        i2 = i2.next
            
    while(i1 != None):
        digSum = carry + i1.val
        addMe = digSum % 10
        carry = digSum // 10
        if (summed == None):
            summed = ListNode(addMe)
            hp = summed
        else:
            summed.next = ListNode(addMe)
            summed = summed.next
        i1 = i1.next
            
            
    while(i2 != None):
        digSum = carry + i2.val
        addMe = digSum % 10
        carry = digSum // 10
        if (summed == None):
            summed = ListNode(addMe)
            hp = summed
        else:
            summed.next = ListNode(addMe)
            summed = summed.next
        i2 = i2.next

    return hp

list1 = ListBuilder().append(3).append(2).append(4).append(5).build()
list2 = ListBuilder().append(9).append(2).append(3).build()


summed = addTwoNumbers(list1, list2)
while(summed != None):
    print(str(summed.val) + "->")
    summed = summed.next
