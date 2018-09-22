def sum_over_min_subarrays(subarrs):
    summed = 0
    for i in range(len(subarrs)):
        min_so_far = subarrs[i]
        for j in range(i, len(subarrs)):
            if subarrs[j] < min_so_far:
                min_so_far = subarrs[j]
            print("min_so_far=%d" % (min_so_far))
            summed += min_so_far
    return summed

print(sum_over_min_subarrays([3,1,2,4]))
