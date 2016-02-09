'''
Created on Dec 6, 2015

@author: bliu
'''
from __builtin__ import False, True
from sys import maxint

class BinaryTree:
    
    def __init__(self, value):
        self.left_child = None
        self.right_child = None
        self.value = value
    
    def setRightChild(self, rightChild):
        self.right_child = rightChild;
        self.right_child.setParent(self)
        
        
    def setLeftChild(self, leftChild):
        self.left_child = leftChild
        self.left_child.setParent(self)
        
    def setParent(self, parent):
        self.parent = parent;
        
    def print_string(self):
        print(self.value)
        
def printBinaryTree(inputTree):
    printBinaryTreeHelper(inputTree, 0)
    
def determine_if_bst(input_tree, min, max):
    if (input_tree is None):
        return True;
    if (input_tree.value < min or input_tree.value > max):
        return False;
    else:
        return determine_if_bst(input_tree.left_child, min, input_tree.value) and determine_if_bst(input_tree.right_child, input_tree.value, max);
       
def printInOrder(input_tree):
    if input_tree is None:
        return None
    if input_tree.right_child is not None:
        current_tree = input_tree.right_child
        while (current_tree.left_child is not None):
            current_tree = current_tree.left_child
        return current_tree.value
    else:
        current_tree = input_tree
        current_parent = input_tree.parent
        while(current_parent is not None and current_tree is current_parent.right_child):
            temp = current_parent
            current_parent = current_parent.parent
            current_tree = temp
        return current_tree
    

def printBinaryTreeHelper(inputTree, depth):
    padding = pad(depth)
    if inputTree is None:
        print padding + "none"
    else:  
        print padding + str(inputTree.value)
        printBinaryTreeHelper(inputTree.left_child, depth+1)
        printBinaryTreeHelper(inputTree.right_child, depth+1)

def pad(length):
    padding = '';
    for x in range (0, length):
        padding += ' ';
    return padding

if __name__ == '__main__':
    binaryTree = BinaryTree(7);
    rightChild = BinaryTree(15);
    leftChild = BinaryTree(3);
    rightLeftChild = BinaryTree(6)
    leftChild.setRightChild(rightLeftChild)
    binaryTree.setLeftChild(leftChild);
    binaryTree.setRightChild(rightChild);  
    print printInOrder(rightLeftChild).value;
