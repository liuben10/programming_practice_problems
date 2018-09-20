def two_sum_help(elems, target):
    elem_set = {}
    for i, e in enumerate(elems):
        elem_set[e] = i

    res = {}
    for i, e in enumerate(elems):
        if (target - e in elem_set and i != elem_set[target-e]):
            res[tuple(sorted([e, target-e]))] = [i, elem_set[target-e]]
            
    return [(tup, res[tup]) for tup in res.keys()]

def two_sum(elems, target):
    sol = two_sum_help(elems, target)
    return [list(s[0]) for s in sol]

def three_sum(elems, target):
    two_sum_set = {}
    for i, e in enumerate(elems):
        two_sums = two_sum_help(elems, target-e)
        for s in two_sums:
            two_sum_set[(tuple(s[0]), tuple(s[1]))] = i
    res = {}
    for i, e in enumerate(elems):
        sols = two_sum_help(elems, target-e)
        for s in sols:
            if ((tuple(s[0]), tuple(s[1])) in two_sum_set and i not in s[1]):
                concatted = [e]
                concatted.extend(list(s[0]))
                
                res[tuple(sorted(concatted))] = 1

    return [list(tup) for tup in res.keys()]
            

elems = [5, 2, 3, 1, 4, 10, 9, 12, 13, 19, 24, 16, 15]
target = 15
print(two_sum(elems, 15))
print(three_sum(elems, 15))
