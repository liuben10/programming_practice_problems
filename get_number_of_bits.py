'''
Created on Jan 31, 2016

@author: bliu
'''


def get_num_of_bits(n):
    cnt = 0
    while n != 0:
        if (n & 1):
            cnt = cnt + 1
        n = n >> 1
    return cnt

def get_diff_in_bits(x,y):
    diff = x ^ y
    return get_num_of_bits(diff)

if __name__ == '__main__':
    print get_diff_in_bits(2, 6)