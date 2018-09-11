'''
Created on Jan 31, 2016

@author: bliu
'''


def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target: 
        print("sum(%s)=%s" % (partial, target))
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n])

def print_matrix(matrix):
    for row in matrix:
        print(row)

def subset_sum_recurs(numbers, target):
    if (target == 0):
        return 1
    if (not numbers):
        return 0
    if (numbers[0] > target):
        return subset_sum_recurs(numbers[1:], target)
    else:
        return subset_sum_recurs(numbers[1:], target-numbers[0]) + subset_sum_recurs(numbers[1:], target)
        
# counts the number of subsets
def subset_sum_dp(numbers, target):
    table = [[0 for i in range(target+1)] for j in range(len(numbers)+1)]
    keeps = [[0 for i in range(target+1)] for j in range(len(numbers)+1)]
    for i in range(len(numbers)+1):
        for j in range(target+1):
            if (j == 0):
                table[i][j] = 1
            elif (i == 0):
                table[i][j] = 0
            elif (numbers[i-1] > j):
                table[i][j] = table[i-1][j]
            else:
                keep = table[i-1][j-numbers[i-1]] if i-1 >= 0 else 0
                if (keep):
                    keeps[i][j] = numbers[i-1]
                skip = table[i-1][j] if i - 1 >= 0 else 0
                table[i][j] = keep + skip
    # print_matrix(table)
    # print("====")
    # print_matrix(keeps)
    return table[len(numbers)][target]
    
                
    


if __name__ == "__main__":
    print(subset_sum_recurs([3,9,8,4],12))
    print(subset_sum_dp([3,9,8,4],12))
    
    
