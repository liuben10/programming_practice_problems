'''
Created on Feb 17, 2016

@author: bliu

Question 62 How do you serialize and deserialize binary trees?
'''

class BinaryTreeNode:
    
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        
def serialize(node, output):
    if (node is None):
        output.append("$")
        return output
    else:
        output.append(node.value)
        serialize(node.left, output)
        serialize(node.right, output)
        return output
    
def deserialize(node, output):
    if (len(output) > 0):
        rootval = output.pop(0)
        if (rootval == "$"):
            return None
        root = BinaryTreeNode(rootval, None, None)
        root.left = deserialize(root.left, output)
        root.right = deserialize(root.right, output)
        return root
    else:
        return node
        
def print_binary_tree(node, padding):
    if (node is None):
        return
    print padding + str(node.value)
    print_binary_tree(node.left, padding + "\t")
    print_binary_tree(node.right, padding + "\t")
        
if __name__ == '__main__':
    bTree = BinaryTreeNode(3, 
                            BinaryTreeNode(4, 
                                                BinaryTreeNode(5, None, None), 
                                                BinaryTreeNode(6, None, None)),
                            BinaryTreeNode(7, None, None))
    output = serialize(bTree, [])
    print output
#     input = [3, 5, 6, 7, 8, 9]
    tree = deserialize(None, output)
    print_binary_tree(tree, "")
    
    
    