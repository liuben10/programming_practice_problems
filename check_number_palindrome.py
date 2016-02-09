'''
Created on Jan 25, 2016

@author: bliu
'''


def check_if_number_is_palindrome(n):
    reverse_of_n = 0
    cnt = n
    while cnt > 0:
        reverse_of_n = reverse_of_n * 10 + cnt % 10
        cnt /= 10
    return reverse_of_n == n

if __name__ == '__main__':
    print check_if_number_is_palindrome(321)