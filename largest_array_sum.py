'''
Created on Mar 1, 2016

@author: bliu
'''

def largest_array_of_sum(input, target):
    if (len(input) == 1):
        return input[0] == target
    tail = 0
    sum_so_far = 0
    head = 0
    largest_array_len = 0
    while head < len(input):
        curHead = input[head]
        if (sum_so_far < target):
            sum_so_far += curHead
        elif (sum_so_far == target):
            cur_array_len = head - tail + 1
            if (cur_array_len > largest_array_len):
                largest_array_len = cur_array_len
            sum_so_far += curHead
        else:
            while (sum_so_far > 2):
                sum_so_far -= input[tail]
                tail = tail + 1   
        head += 1
    return largest_array_len
                
                
    
if __name__ == '__main__':
    print largest_array_of_sum([0, 1, 1, 0, 1, -1, 0, 1], 2)