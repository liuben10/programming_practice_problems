'''
Created on Feb 17, 2016

@author: bliu
'''

from binary_tree_construction_problem import construct

class BinaryTreeNode:
    
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def print_from_top_to_bottom(node):
    if (node is None):
        return
    queue = []
    queue.append(node)
    while (len(queue) > 0):
        top_node = queue.pop(0)
        print (top_node.value)
        if (top_node.left is not None):
            queue.append(top_node.left)
        if (top_node.right is not None):
            queue.append(top_node.right)
            
if __name__ == '__main__':
    tree = construct([1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6])
    print_from_top_to_bottom(tree)    