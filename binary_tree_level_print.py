'''
Created on Feb 17, 2016

@author: bliu

Please print a binary tree from its top level to bottom level, and print nodes at the same level from left to right.
'''

class BinaryTreeNode:
    
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
'''
Print top to bottom in serial
'''
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
'''
Print top to bottom level by level
'''
def print_from_top_to_bottom_one_level(node):
    if (node is None):
        return
    queue = []
    queue.append([node, 0])
    result = [[]]
    curlevel = 0
    while (len(queue) > 0):
        top_tuple = queue.pop(0)
        top_node = top_tuple[0]
        level = top_tuple[1]
        if (level != curlevel):
            result.append([top_node.value])
            curlevel += 1
        else:
            result[curlevel].append(top_node.value)
        if (top_node.left is not None):
            queue.append([top_node.left, level+1])
        if (top_node.right is not None):
            queue.append([top_node.right, level+1])
    for e in result:
        print str(e) + "\n"
            
if __name__ == '__main__':
    bTree = BinaryTreeNode(3, 
                        BinaryTreeNode(4, 
                                        BinaryTreeNode(5, None, None), 
                                        BinaryTreeNode(6, None, None)),
                        BinaryTreeNode(7, BinaryTreeNode(8, None, None), None))
    print_from_top_to_bottom_one_level(bTree)    