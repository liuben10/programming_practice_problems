

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
    componentified = {}
    for component in components:
        treeify(component, component_trees)
        componentified[component] = 1

    curtree = None
    curtreeIdx = 0
    res = []
    components_eval = {}
    component_so_far = ""
    for i, c in enumerate(stringin):
        if (c in component_trees and curtree is None):
            curtree = component_trees[c]
            curtreeIdx = i
            component_so_far += c
        elif curtree is not None and c not in curtree.children:
            if (not curtree.children):
                if (not component_so_far in components_eval):
                    components_eval[component_so_far] = 1
                if (components_eval.keys() == componentified.keys()):
                    res.append(curtreeIdx)
                    curtree = None
                    curtreeIdx = -1
                    component_so_far = ""
                    components_eval = {}
                else:
                    if (c in component_trees):
                        curtree = component_trees[c]
                        component_so_far = c
                    else:
                        curtree = None
                        component_so_far = ""
                        components_eval = {}
            else:
                curtree = None
                curtreeIdx = -1
                component_so_far = ""
                components_eval = {}
        elif curtree is not None and c in curtree.children:
            curtree = curtree.children[c]
            component_so_far += c
    return res

print(indexes_of_concatenation("barfoofazthefoofazbarman", ["foo", "bar", "faz"]))
