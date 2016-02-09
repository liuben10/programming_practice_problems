'''
Created on Dec 20, 2015

@author: bliu
'''
from macpath import curdir


def slow_fib(n):
    if (n <= 1):
        return n
    else:
        return slow_fib(n-1) + slow_fib(n-2)
    
def fast_fib(n):
    prev = 0
    cur = 0
    cursum = 0
    i = 0
    while i < n:
        i += 1
        if i == 1:
            cursum = 1
        else:
            tmp = cur
            cur = cursum
            prev = tmp
            cursum = cur + prev        
    return cursum

if __name__ == '__main__':
    for i in range(0, 10):
        print str(i) + ": " + str(fast_fib(i))