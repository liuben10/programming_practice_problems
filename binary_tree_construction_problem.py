'''
Created on Feb 15, 2016

@author: bliu

Please build a binary tree with a pre-order traversal sequence and an in-order traversal sequence. All elements in these two given sequences are unique.
For example, if the input pre-order traversal sequence is {1, 2, 4, 7, 3, 5, 6, 8} and in-order traversal order is {4, 7, 2, 1, 5, 3, 8, 6}, the built tree is shown in Figure 6-13.
'''


class BinaryTreeNode:
    
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        
    
def constructCore(pre_order, in_order):
    print str(pre_order) + ", " + str(in_order)
    if (pre_order == [] and pre_order == in_order):
        return
    rootValue = pre_order[0]
    root = BinaryTreeNode(rootValue, None, None)
    if (pre_order[0] == pre_order[-1:]):
        if (in_order[0] == in_order[-1:] and pre_order[0] == in_order[0]):
            return root
        else:
            raise Exception("exception was thrown")
            return
    cnt = 0
    in_val = in_order[cnt]
    while(cnt < len(in_order) and in_val != rootValue):
        cnt += 1
        in_val = in_order[cnt]
    print cnt
    if cnt == len(in_order)-1 and in_val != rootValue:
        raise Exception("exception was thrown")
    if (cnt > 0):
        root.left = constructCore(pre_order[1:cnt+1], in_order[0:cnt])
    if (cnt < len(pre_order)):
        root.right = constructCore(pre_order[cnt+1:len(pre_order)], in_order[cnt+1:len(in_order)])
    return root

def print_binary_tree(node, padding):
    if (node is None):
        return
    print padding + str(node.value)
    print_binary_tree(node.left, padding + "\t")
    print_binary_tree(node.right, padding + "\t")
    
def construct(pre_order, in_order):
    if pre_order is None or in_order is None or len(pre_order) != len(in_order):
        return None
    else:
        return constructCore(pre_order, in_order)
    
if __name__ == '__main__':
    tree = construct([1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6])
    print_binary_tree(tree, "")