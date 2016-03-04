'''
Created on Mar 2, 2016

@author: bliu
'''
def swap(input, src, dest):
    tmp = input[src]
    input[src] = input[dest]
    input[dest] = tmp

def bubble_sort(input):
    for i in range(len(input), 0, -1):
        maxSoFar = input[0]
        for j in range(i):
            if (maxSoFar > input[j]):
                swap(input, j-1, j)
            else:
                maxSoFar = input[j]
                
    return input

if __name__ == '__main__':
    print bubble_sort([3, 2, 4, 9, 6, 8])