# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printListNode(listN):
    res = ""
    while(listN is not None):
        res += str(listN.val) + ", "
        listN = listN.next
    print(res)
    
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        resList = None
        while(l1 is not None and l2 is not None):
            raw_sum = l1.val + l2.val + carry
            carry = raw_sum // 10
            summed = raw_sum % 10
            if (resList is None):
                resList = ListNode(summed)
                hp = resList
            else:
                resList.next = ListNode(summed)
                resList = resList.next
            l1 = l1.next
            l2 = l2.next
        
        while(l1 is not None):
            raw_sum = l1.val + carry
            summed = raw_sum % 10
            carry = raw_sum // 10
            if (resList is None):
                resList = ListNode(summed)
                hp = resList
            else:
                resList.next = ListNode(summed)
                resList = resList.next
            l1 = l1.next
            
        while(l2 is not None):
            raw_sum = l2.val + carry
            summed = raw_sum % 10
            carry = raw_sum // 10
            if (resList is None):
                resList = ListNode(summed)
                hp = resList
            else:
                resList.next = ListNode(summed)
                resList = resList.next
            l2 = l2.next
        while(carry != 0):
            summed = carry % 10
            carry = carry // 10
            resList.next = ListNode(summed)
            resList = resList.next
        return hp


s = Solution()
a = ListNode(5)

b = ListNode(5)

printListNode(s.addTwoNumbers(a, b))
