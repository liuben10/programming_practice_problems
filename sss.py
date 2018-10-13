def subset_sum_recurs(nodes, i, target):
    print("%s, i=%s, target=%s" % (nodes, i, target))
    if (target == 0):
        return 1
    if (i == 0):
        return 0
    elif (nodes[i-1] > target):
        return subset_sum_recurs(nodes, i-1, target)
    else:
        return subset_sum_recurs(nodes, i-1, target) + subset_sum_recurs(nodes, i-1, target-nodes[i-1])

def subset_sum_recurs_paths(nodes, i, target, listSoFar=[]):
    if (target == 0):
        print(listSoFar)
        return 1
    if (i == 0):
        return 0
    elif (nodes[i-1] > target):
        return subset_sum_recurs_paths(nodes, i-1, target, listSoFar)
    else:
        return subset_sum_recurs_paths(nodes, i-1, target, listSoFar) + subset_sum_recurs_paths(nodes, i-1, target-nodes[i-1], listSoFar + [nodes[i-1]])

# print(subset_sum_recurs([3, 2, 1], 3, 6))
testIn = [1, 19, 25, 99, 181, 33, 22, 11, 99, 13, 77]
print(subset_sum_recurs_paths(testIn, len(testIn), 100))
