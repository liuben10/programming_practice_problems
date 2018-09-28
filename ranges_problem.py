def ranges_problem(ranges, toIns):
    actuallyInserting = toIns
    result_ranges = []
    ad_flag = True
    for r in ranges:
        if r[0] < actuallyInserting[0] and r[1] > actuallyInserting[0]:
            actuallyInserting[0] = r[0]
        if r[0] < actuallyInserting[1] and r[1] > actuallyInserting[1]:
            actuallyInserting[1] = r[1]
        if r[1] < actuallyInserting[0] or r[0] > actuallyInserting[1]:
            result_ranges.append(r)
        else:
            if ad_flag:
                result_ranges.append(actuallyInserting)
                ad_flag = False
    return result_ranges
            
            
            

print(ranges_problem([[0, 2], [3, 5], [9, 16], [17, 23]], [6, 13]))
