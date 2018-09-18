from functools import reduce

def swap(perm, i, j):
    tmp = perm[i]
    perm[i] = perm[j]
    perm[j] = tmp
    return perm

def find_min(perms):
    (idx, minimum) = (-1, float('inf'))
    for i, p in enumerate(perms):
        if p < minimum:
            idx = i
            minimum = p
    return (idx, minimum)
            
        
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
            (idx, miny) = find_min(permutation[1:])
            print("idx=%d, miny=%d" % (idx+1, miny))
            swapped = swap(permutation, 0, idx+1)
            return [swapped[0]] + next_permutation(swapped[1:])
        else:
            return [first] + next_permutation(permutation[1:])
        
print(next_permutation([1,3,2]))
# print(next_permutation([1,3,2]))
