'''
Created on Dec 20, 2015

@author: bliu
'''

def swap(src, dest, input):
    tmp = input[src]
    input[src] = input[dest]
    input[dest] = tmp

def smallest_missing_positive_integer(input):
    smallest_missing = 0
    for i in range(len(input)):
        if (input[i] >= len(input)):
            continue
        if (input[i] >= 0):
            swap(input[i], i, input)   
    for i in range(len(input)):
        if (input[i] < 0):
            continue
        if (input[i] == smallest_missing):
            smallest_missing += 1
        else:
            break
    return smallest_missing
    
    
if __name__ == '__main__':
    print smallest_missing_positive_integer([0, -5, 1, 2, 0, 3, -5])
    