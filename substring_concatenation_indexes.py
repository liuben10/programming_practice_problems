

class RadixTreeNode:

    def __init__(self, val):
        self.val = val
        self.children = {}

    def print_tree(self):
        self.print_tree_helper(0)

    def print_tree_helper(self, pad):
        padding = "="*pad
        print (padding + self.val)
        for childtree in self.children.values():
            childtree.print_tree_helper(pad+1)

    
    def add_child(self, val):
        added = RadixTreeNode(val)
        self.children[val] = added
        return added
        

def treeify(component, component_trees):
    comp_idx = 1
    child = None
    for tree in component_trees.values():
        if (tree.val == component[0]):
            child = tree
    if (child is None):
        child = RadixTreeNode(component[0])
        component_trees[component[0]] = child
    while comp_idx < len(component):
        if (component[comp_idx] in child.children):
            child = child.children[component[comp_idx]]
        else:
            child = child.add_child(component[comp_idx])
        comp_idx += 1
            
    

def indexes_of_concatenation(stringin, components):
    component_trees = {}
    for component in components:
        treeify(component, component_trees)

    curtree = None
    curtreeIdx = 0
    res = []
    for i, c in enumerate(stringin):
        if (c in component_trees and curtree is None):
            curtree = component_trees[c]
            curtreeIdx = i 
        elif curtree is not None and c not in curtree.children:
            if (not curtree.children):
                res.append(curtreeIdx)
            curtree = None
            curtreeIdx = -1
        elif curtree is not None and c in curtree.children:
            curtree = curtree.children[c]
    return res

print(indexes_of_concatenation("barfoothefoobarman", ["foo", "bar", "faz"]))
