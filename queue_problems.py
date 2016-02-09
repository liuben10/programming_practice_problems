'''
Created on Dec 12, 2015

@author: bliu
'''
from __builtin__ import None

class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        
class Queue:
    def __init__(self):
        self.size = 0
        self.hp = None
        self.tp = None
    
    def isEmpty(self):
        return self.size == 0
    
    def peek(self):
        return self.tp
    
    def pop(self):
        new_end = None
        iter_node = self.hp
        while(iter_node.next_node is not None):
            new_end = iter_node
            iter_node = iter_node.next_node
        self.tp = new_end
        self.tp.next_node = None
        
    def push(self, node):
        if (self.hp is None):
            self.hp = node
        else:
            tmp = self.hp
            self.hp = node
            node.next_node = tmp
    
        
    
class Stack:
    
    def __init__(self):
        self.size = 0
        self.hp = None
        
    def isEmpty(self):
        return self.hp is None
    
    def peek(self):
        return self.hp
        
    def push(self, node):
        if (self.hp is None):
            self.hp = node
        else:
            node.next_node = self.hp
            self.hp = node
        self.size += 1
        
    def pop(self):
        if (self.hp is None):
            self.size = 0
            return None
        else:
            tmp = self.hp
            self.hp = self.hp.next_node
            self.size -= 1
            return tmp

class Queue_With_Stack:
    def __init__(self):
        self.front_stack = Stack();
        self.back_stack = Stack();
    
    def push(self, node):
        self.front_stack.push(node)
        
    def pop(self):
        if (self.back_stack.isEmpty()):
            while (self.front_stack.size > 0):
                head = self.front_stack.peek()
                self.front_stack.pop()
                self.back_stack.push(head)
        if self.back_stack.size == 0:
            print "deque called on empty queue"
            pass
        head = self.back_stack.peek()
        self.back_stack.pop()
        return head
    
if __name__ == '__main__':
    q = Queue_With_Stack()
    q.push(Node(3))
    q.push(Node(4))
    q.push(Node(5))
    print q.pop().value
    print q.pop().value
    print q.pop().value
            