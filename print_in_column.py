'''
Created on Feb 27, 2016

@author: bliu
'''

class TreeNode:
    
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def printColsOutOfOrder(rootT):
    colMap = {}
    collectCols(rootT, 0, colMap)
    print colMap
    
    
def collectCols(rootT, count, colMap):
    if (rootT is None):
        return
    if count in colMap.keys():
        colMap[count].append(rootT.value)
    else:
        colMap[count] = [rootT.value]
    collectCols(rootT.left, count+1, colMap)
    collectCols(rootT.right, count-1, colMap)
        
def printTree(root, padding):
    if (root is None):
        return 
    print  padding + str(root.value)
    printTree(root.left, "\t" + padding )
    printTree(root.right, "\t" + padding)

if __name__ == '__main__':
    root = TreeNode(6, TreeNode(3, TreeNode(2, TreeNode(4, None, None), TreeNode(7, None, TreeNode(8, None, None))), TreeNode(1, None, None)), TreeNode(5, None, TreeNode(9, TreeNode(3, None, None), TreeNode(7, None, None))))
    printColsOutOfOrder(root)   
    