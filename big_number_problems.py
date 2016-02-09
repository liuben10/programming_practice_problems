'''
Created on Feb 4, 2016

@author: bliu
'''
import math


def increment(number_to_print):
    carry_bit = 0
    last_index = len(number_to_print) - 1
    if (int(number_to_print[last_index]) + 1 is 10):
        carry_bit = 1
        number_to_print[last_index] = "0"    
    else:
        number_to_print[last_index] = str(int(number_to_print[last_index]) + 1)
    last_index -= 1
    while (carry_bit):
        if (last_index < 0):
            number_to_print.insert(0, "1")
            carry_bit = 0
        elif (int(number_to_print[last_index]) + 1 is 10):
            carry_bit = 1
            number_to_print[last_index] = "0"
        else:
            carry_bit = 0
            number_to_print[last_index] = str(int(number_to_print[last_index]) + 1)
        last_index -= 1
    return number_to_print

    




def big_number_problem(max_size):
    number_to_print = []
    while len(number_to_print) < max_size:
        if len(number_to_print) == 0:
            number_to_print = ["0"]
            print number_to_print
        else:
            print increment(number_to_print)
            
        
if __name__ == '__main__':
    big_number_problem(100)