'''
Created on Dec 12, 2015

@author: bliu
'''
import math


def bin_search(test_in, item):
    min_val = 0
    max_val = len(test_in)
    while(min_val < max_val):
        mid = (min_val + max_val) / 2
        print mid
        if (item == test_in[mid]):
            return True
        if item > test_in[mid]:
            min_val = mid+1
        else:
            max_val = mid
    return False

if __name__ == '__main__':
    test_in = [2, 4, 5, 6, 7, 8]
    print bin_search(test_in, 7)