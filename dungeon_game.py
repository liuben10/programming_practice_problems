def min_health(dungeon):
    rows = len(dungeon)
    cols = len(dungeon[0])
    fringe = []
    fringe.append(((rows-1, cols-1), 1))
    min_health = float("inf")
    while(fringe):
        visiting, min_health_so_far = fringe.pop(len(fringe)-1)
        print("visiting={}, health={}".format(visiting, min_health_so_far))
        ridx = visiting[0]
        cidx = visiting[1]
        effect = dungeon[visiting[0]][visiting[1]]
        new_min = max(min_health_so_far + -effect, 1)
        if (ridx == 0 and cidx == 0):
            min_health = min(min_health, new_min)
        if ridx > 0:
            fringe.append(((ridx-1, cidx), new_min))
        if cidx > 0:
            fringe.append(((ridx, cidx-1), new_min))
    return min_health

dungeon = [
    [-1, -2, 3, -4]
]
dungeon1 = [
    [-1, 1]
]
# dungeon = [
#     [-2, -3, 3],
#     [-5, -10, 1],
#     [10, 30, -5]
# ]
