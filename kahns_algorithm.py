def kahns_algorithm(nodes, edges):
    ordered = []
    exploring_nodes = [i for i in range(nodes) if i not in [e[1] for e in edges]]
    while exploring_nodes:
        node = exploring_nodes.pop(0)
        ordered.append(node)
        for m, e in [(e[1], e) for e in edges if e[0] == node]:
            edges.remove(e)
            if m not in [e[1] for e in edges]:
                exploring_nodes.append(m)
    if edges:
        return -1
    else:
        return ordered
    

print(kahns_algorithm(4, [[0,1], [2, 1], [2, 3], [2, 0]]))


