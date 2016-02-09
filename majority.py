'''
Created on Jan 23, 2016

@author: bliu
'''


def majority(input):
    times = 0
    majority = input[0]
    for e in input:
        if times == 0:
            majority = e
            times += 1
        elif e == majority:
            times += 1
        else:
            times -= 1
    if times <= 0:
        return -1
    return majority
    
    
if __name__ == '__main__':
    print majority([1, 2, 2, 4, 3, 3, 2, 4])