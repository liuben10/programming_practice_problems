'''
Created on Dec 26, 2015

@author: bliu
'''

'''The trick to this problem is to realize that the search condition is changed.  Now, instead of searching on whether the element
is greater than or less than the mid, it is to search on the 'bucket' with the 'bucket' being ordered by the value of the ends'''
def find_min_in_rotated(input):
    high = len(input) - 1
    low = 0
    while(low < high):
        mid = (high + low) / 2
        if (input[mid] > input[mid+1]):
            return input[mid+1]
        if input[mid] < input[low]:
            high = mid
        else:
            low = mid+1
    return -1

'''
problem is given a unimodal array input, i.e. [1, 2, 3, 4, 5, 3, 2, 1], find the maximum number (i.e. the turning number), in O(lg(n)) time.
Trick is to compare the two numbers on either side of the mid point, and determine if they go from increasing to decreasing, if not,
then you must compare which side (increasing or decreasing) side they are on and do the binary search accordingly.
'''
def turning_number(input):
    high = len(input) - 1
    low = 0
    while(low < high):
        mid = (high + low) / 2
        if (input[mid] > input[mid + 1] and input[mid] >= input[low] and input[mid+1] >= input[high]):
            return mid
        if (input[mid] < input[mid + 1]):
            low = mid+1
        else:
            high = mid
    return -1
    
    
if __name__ == '__main__':
    print turning_number([3, 5, 7, 9, 2])