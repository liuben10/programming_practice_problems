'''
Created on Jan 28, 2016

@author: bliu
'''

def swap(in_arr, src, dest):
    tmp = in_arr[dest]
    in_arr[dest] = in_arr[src]
    in_arr[src] = tmp

def odd_before_even(test_in):
    p1 = 0
    p2 = len(test_in) - 1
    p1_element = test_in[p1]
    p2_element = test_in[p2]
    while p1 < p2:
        while (not p2_element % 2 and p1 < p2):
            p2 -= 1
            p2_element = test_in[p2]
        while (p1_element % 2 and p1 < p2):
            p1 += 1
            p1_element = test_in[p1]
        swap(test_in, p1, p2)
        p2_element = test_in[p2]
        p1_element = test_in[p1]
    
if __name__ == '__main__':
    test_in = [1, 2, 3, 4, 6, 7]
    odd_before_even(test_in)
    print test_in