'''
Created on Jan 27, 2016

@author: bliu
'''

def fast_power(x, y):
    if (y == 0):
        return 1
    if (y == 1):
        return x
    if (y % 2 == 0):
        power = fast_power(x, y/2)
        return power*power
    else:
        return x * fast_power(x, y-1)
    
    
if __name__ == '__main__':
    print fast_power(10, 3)