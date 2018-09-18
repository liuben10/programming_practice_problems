from functools import reduce

def swap(perm, i, j):
    tmp = perm[i]
    perm[i] = perm[j]
    perm[j] = tmp
    return perm

def find_next(elem, perms):
    pidx = -1
    nextp = None
    for i, p in enumerate(perms):
        if p > elem and (nextp is None or p < nextp) :
            nextp = p
            pidx = i
    return (pidx, nextp)
        
            
        
def is_sorted(permutation):
    prev = permutation[0]
    for elem in permutation:
        if (elem > prev):
            return False
        prev = elem
    return True

def next_permutation(permutation):
    if (len(permutation) == 1):
        return [permutation[0]]
    else:
        first = permutation[0]
        if (first > permutation[1] and is_sorted(permutation[1:])):
            return permutation[::-1]
        elif is_sorted(permutation[1:]):
            (idx, miny) = find_next(first, permutation[1:])
            swapped = swap(permutation, 0, idx+1)
            return [swapped[0]] + sorted(swapped[1:])
        else:
            return [first] + next_permutation(permutation[1:])
        
print(next_permutation([1,2,3]))
print(next_permutation([1,3,2]))
print(next_permutation([2,3,1]))
print(next_permutation([3,2,1]))
