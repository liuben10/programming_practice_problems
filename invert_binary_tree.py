class BinaryTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def setLeft(self, value):
        self.left = BinaryTree(value)
        return self.left

    def setRight(self, value):
        self.right = BinaryTree(value)
        return self.right


def print_tree(btree, pad):
    padding = "".join("-" for i in range(pad))
    if (btree is None):
        return padding + "EMPTY"
    else:
        return padding + str(btree.value) + "\n" + print_tree(btree.left, pad+1) + "\n" + print_tree(btree.right, pad+1)
    
def invert(btree):
    nodes_to_visit = []
    result_tree = None
    nodes_to_visit.append((btree, result_tree, False))
    while(nodes_to_visit):
        visiting, parent, is_left = nodes_to_visit.pop(len(nodes_to_visit) - 1)
        if (parent is None):
            result_tree = visiting
        else:
            if (is_left):
                parent.right = visiting
            else:
                parent.left = visiting
        if visiting.left is not None:
            nodes_to_visit.append((visiting.left, visiting, True))
        if visiting.right is not None:
            nodes_to_visit.append((visiting.right, visiting, False))
    return btree


a = BinaryTree(1)
b = a.setLeft(2)
c = a.setRight(3)
d = b.setLeft(4)
e = b.setRight(5)
f = c.setLeft(6)
g = c.setRight(7)
d.setLeft(8)

print(print_tree(a, 0))

inverted = invert(a)
print(print_tree(inverted, 0))
# print(layers)
