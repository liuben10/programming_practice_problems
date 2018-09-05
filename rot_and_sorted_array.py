def find_min_rot_and_sorted(array):
    if (len(array) == 1):
        return array[0]
    low = 0
    high = len(array)
    while(low < high):
        mid = (low + high) // 2
        if (mid-1 >= 0 and mid+1 < len(array) and array[mid-1] > array[mid] and array[mid+1] > array[mid] or
            mid is 0 and mid+1 < len(array) and array[mid] < array[mid+1] or
            mid is len(array)-1 and mid-1 >= 0 and array[mid] < array[mid-1]):
            return array[mid]
        elif (array[mid] > array[0] and array[mid] > array[len(array)-1]):
            low = mid
        else:
            high = mid-1
    return -1



print(find_min_rot_and_sorted([12, 15, 18, 19, 2, 3]))
