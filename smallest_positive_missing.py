def swap(intarray, src, dest):
    tmp = intarray[src]
    intarray[src] = intarray[dest]
    intarray[dest] = tmp

    
def first_missing_positive(intarray):
    if (len(intarray) == 1):
        if (intarray[0] == 1):
            return 2
        else:
            return 1

    copy = intarray
    for i, elem in enumerate(intarray):
        if elem > 0:
            if elem <= len(intarray):
                swap(copy, i, elem-1)
    print(copy)

    tracking = False
    prev = 1
    for elem in copy:
        if (tracking):
            if (elem != prev+1):
                return prev+1
            prev = elem
        elif (elem == 1):
            tracking = True
    
    return len(intarray) + 1 if tracking else 1


print(first_missing_positive([1, 2, 0]))
print(first_missing_positive([3, 4, -1, 1]))
print(first_missing_positive([7,8,9,11,12]))
print(first_missing_positive([1,2,3,4,56,7,8]))
        
        
