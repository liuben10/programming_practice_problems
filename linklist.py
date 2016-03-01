

class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    
    def __init__(self, node):
        self.hp = Node(node)
        
    def recursive_reverse(self):
        if (self.hp.next is None):
            return self.hp
        else:
            tmp = self.hp
            rest = tmp.next
            self.hp = rest
            last_node = self.recursive_reverse()
            last_node.next = tmp
            tmp.next = None
            return tmp
        
    def reverse(self):
        head = self.hp
        prev = None
        tmp = None
        while (head is not None):
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        self.hp = prev

    def print_self(self):
        iter = self.hp  # @ReservedAssignment
        while (iter is not None):
            print iter.value
            iter = iter.next  # @ReservedAssignment
            
    def add_to_front(self, value):
        node = Node(value)
        node.next = self.hp
        self.hp = node
        
def recursive_reverse(node):
    hp = node
    if hp.next is None:
        return hp
    else:
        tmp = hp
        rest = hp.next
        reversed_list = recursive_reverse(rest)
        reversed_list.next = tmp
        tmp.next = None
        return tmp
        
if __name__ == '__main__':
    ll = LinkedList(12)
    ll.add_to_front(13)
    ll.add_to_front(14)
    ll.recursive_reverse()
    ll.print_self()
            