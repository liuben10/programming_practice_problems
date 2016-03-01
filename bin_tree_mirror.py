'''
Created on Feb 20, 2016

@author: bliu
'''


class BinaryTreeNode:

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        
        
'''
Mirror recursive. Very easy.
'''
def get_mirrored_tree(bTree):
    if (bTree is None):
        return bTree
    else:
        mirrored_left =  get_mirrored_tree(bTree.left)
        mirrored_right = get_mirrored_tree(bTree.right)
        bTree.left = mirrored_right
        bTree.right = mirrored_left
        return bTree
    
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
        mirroredBtree = get_mirrored_tree(bTree)
        print_binary_tree(mirroredBtree, "")
        
        