def level_order_traversal(btree):
    fringe = []
    idx = 0
    fringe.insert(0, (idx, 0))
    levels = []
    while (fringe):
        (idx, lvl) = fringe.pop(len(fringe)-1)
        if (lvl >= len(levels)):
            levels.append([btree[idx]])
        else:
            levels[lvl].append(btree[idx])
        left = 2 * idx + 1
        right = 2 * idx + 2
        if (left < len(btree) and btree[left] is not None):
            fringe.insert(0, (left, lvl+1))
        if (right < len(btree) and btree[right] is not None):
            fringe.insert(0, (right, lvl+1))
    return levels
            
            


print(level_order_traversal([5, 9, 12, None, None, 18, 99]))
