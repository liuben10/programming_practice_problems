'''
Created on Jan 31, 2016

@author: bliu
'''


def get_non_duplicate(input):
    value = 0
    for n in input:
        value = value ^ n
    return value


def get_partition(input, flag):
    partition = []
    for n in input:
        if n & flag:
            partition.append(n)
    return partition


def get_all_non_duplicated_numbers(input):
    value = 0
    for n in input:
        value = value ^ n
    partitions = []
    flag = 1
    cnt = 0
    while cnt < len(input):
        if (value & flag):
            partition = get_partition(input, flag)
            partitions.append(partition)
        flag = flag << 1
        cnt += 1
    results = []
    for partition in partitions:
        results.append(get_non_duplicate(partition))
    return results

if __name__ == '__main__':
    print get_all_non_duplicated_numbers([1, 1, 2, 5, 5, 3, 4, 4])
    
    print get_all_non_duplicated_numbers([1, 1, 2])