'''
Created on Dec 12, 2015

@author: bliu
'''
import random
from test.test_sax import start

#         if (test_in[lptr] > pivot):
#             while test_in[rptr] > pivot:
#                 rptr--
#             swap(test_in, lptr, rptr)
#         else:
#             lptr++

def swap(array, a, b):
    tmp = array[a]
    array[a] = array[b]
    array[b] = tmp

def partition(test_in, start, end):
    print ("partition=" + str(test_in) + ", " + str(start) + ", " + str(end))
    pivot = random.randint(start, end)
    print "selected pivot=" + str(pivot)
    swap(test_in, pivot, end)
    small = start - 1
    for i in range(start, end):
        if (test_in[i] < test_in[end]):
            small += 1
            if (i != small):
                swap(test_in, small, i)
            
    small += 1
    if (small != end):
        swap(test_in, small, end)
    return small


def quicksort(input, start, end):
    if (start == end):
        return
    pivot_index = partition(input, start, end)
    print "pivot_index=" + str(pivot_index)
    if (start != pivot_index):
        quicksort(input, start, pivot_index-1)
    if (end != pivot_index):
        quicksort(input, pivot_index+1, end)
    
if __name__ == '__main__':
    test_in = [4, 3, 5, 8, 2, 3]
    quicksort(test_in, 0, 5)
    print test_in
    