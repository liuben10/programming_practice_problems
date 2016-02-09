'''
Created on Jan 27, 2016

@author: bliu
'''


def bin_search(input_array, num_to_find):
    low = 0
    high = len(input_array) - 1
    while low < high:
        mid = (low + high) / 2
        if (input_array[mid] == num_to_find):
            return True
        elif (num_to_find < input_array[mid]):
            high = mid
        else:
            low = mid + 1
    return False


def find_number_in_sorted_2d_matrix(input_matrix, num_to_find):
    low = 0;
    high = len(input_matrix) - 1
    while low < high:
        mid = (low + high) / 2
        first_mid = input_matrix[mid][0]
        last_mid = input_matrix[mid][len(input_matrix[mid])-1]
        if num_to_find >= first_mid and num_to_find <= last_mid:
            return bin_search(input_matrix[mid], num_to_find)
        elif num_to_find < first_mid:
            high = mid
        else:
            low = mid+1
    return False

if __name__ == '__main__':
    print find_number_in_sorted_2d_matrix([[1 ,2, 3], [4, 5, 6], [7, 8, 9]], 10)
            