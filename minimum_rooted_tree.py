def height(root, edges):
    height = 0
    explore = [(root, 0)]
    visited = {}
    max_height = float('-inf')
    while explore:
        (node, height) = explore.pop(0)
        visited[node] = 1
        if (height > max_height):
            max_height = height
        succ = [e[1] for e in edges if e[0] == node]
        succ.extend([e[0] for e in edges if e[1] == node])
        for s in succ:
            if s not in visited:
                explore.append((s, height+1))
    return max_height
        
    

def minimum_rooted_tree(nodes, edges):
    min_height = float('inf')
    minimum_rooted_nodes = []
    for i in range(nodes):
        curh = height(i, edges)
        if (curh < min_height):
            min_height = curh
            minimum_rooted_nodes = [i]
        elif curh == min_height:
            minimum_rooted_nodes.append(i)
    return minimum_rooted_nodes

    

print(minimum_rooted_tree(4, [[1,0], [1,2], [1,3]]))
print(minimum_rooted_tree(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))



    
