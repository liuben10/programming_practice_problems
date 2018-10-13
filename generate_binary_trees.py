class BinaryTree:
    def __init__(self, buf):
        self.buf = buf

    def insert(self, val):
        prev = -1
        i = 0
        while i < len(self.buf):
            lIdx = 2 * i + 1
            rIdx = 2 * i + 2
            if self.buf[i] > val:
                    if lIdx >= len(self.buf):
                        extended = [None for i in range(2 * len(self.buf))]
                        self.buf = self.buf + extended
                        self.buf[lIdx] = val
                        return self
                    if self.buf[lIdx] is None:
                        self.buf[lIdx] = val
                        return self
                    else:
                        prev = i
                        i = lIdx
            else:
                    if rIdx >= len(self.buf):
                        extended = [None for i in range(2 * len(self.buf))]
                        self.buf = self.buf + extended
                        self.buf[rIdx] = val
                        return self
                    elif self.buf[rIdx] is None:
                        self.buf[rIdx] = val
                        return self
                    else:
                        prev = i
                        i = rIdx

    def to_pretty_str(self):
        return self.to_pretty_str_help(0, 0)

    def to_pretty_str_help(self, cur, pad):
        padding = "".join(["-" for i in range(pad)])
        if cur < len(self.buf):
            res = padding + str(self.buf[cur]) + "\n"
            if (self.buf[cur] is not None):
                res += self.to_pretty_str_help(2 * cur + 1, pad+1)
                res += self.to_pretty_str_help(2 * cur + 2, pad+1)
            return res
        else:
            return padding + "None\n"

def gen_binary_trees(n):
    nodes = [i for i in range(n)]
    return gen_binary_trees_helper(nodes, n)

def gen_binary_trees_helper(nodes, size):
    if (size == 1):
        return [(BinaryTree([n]), {n: 1}) for n in nodes]
    else:
        results = gen_binary_trees_helper(nodes, size-1)
        res = []
        for tree, elems in results:
            uninsed = [f for f in nodes if f not in elems]
            for u in uninsed:
                insed_copy = BinaryTree(tree.buf)
                insed_copy.insert(u)
                e_copy = {}
                e_copy.update(elems)
                e_copy[u] = 1
                res.append((insed_copy, e_copy))
        return res


def structure_preorder(btree):
    idx = 0
    while idx < len(btree.buf):
        
            
    



inserted = BinaryTree([5]).insert(4).insert(9).insert(11).insert(12).insert(15).insert(3).insert(2)
# inserted = BinaryTree([5]).insert(4).insert(9).insert(13)

for tree, elems in gen_binary_trees_helper([0, 1, 2], 3):
    print(tree.buf)
