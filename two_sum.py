def two_sum(nums, target):
    diffs = {}
    indices = []
    for i, num in enumerate(nums):
        diffs[num] = i

    res = []

    for i, num in enumerate(nums):
        if (target - num in diffs):
            res.append(i)
            res.append(diffs[target - num])
            return res

    return res

print(two_sum([2, 3, 5, 9], 7))
        
