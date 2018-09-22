'''
Created on Jan 25, 2016

@author: bliu
'''

'''
This is for array of elements 0..n-2
'''
def find_single_duplicated_element(input):
    unaffected_sum = 0
    affected_sum = 0
    n = len(input)
    for i in range(0, n-1):
        unaffected_sum += i
    for e in input:
        affected_sum += e
    return affected_sum - unaffected_sum


def swap(input, src, dest):
    tmp = input[dest]
    input[dest] = input[src]
    input[src] = tmp
'''
Trick to this problem is to keep cur on the current index if the current element in that position is not equal to the index.
'''
def find_a_duplicated_element(input):
    if (len(input) == 1):
        return -1
    cur = 0
    while cur < len(input):
        if (cur != input[cur]):
            if (input[input[cur]] == input[cur]):
                return input[cur]
            swap(input, cur, input[cur])
        else:
            cur += 1
    return -1

def print_array_in_increasing_order_from_mid(array):
    N = len(array)
    lp = 0
    hp = 0
    if (N % 2 == 0):
        lp = N // 2
        hp = lp + 1
    else:
        lp = N // 2
        hp = N // 2

    while(lp >= 0 or hp < N):
        if (lp < 0):
            print(array[hp])
            hp += 1
        elif (hp >= N):
            print(array[lp])
            lp -= 1
        else:
            if (array[hp] > array[lp]):
                print(array[hp])
                hp += 1
            else:
                print(array[lp])
                lp -= 1
                
                
    
    
if __name__ == "__main__":
    # print(find_a_duplicated_element([3, 1,1, 0]))
    print_array_in_increasing_order_from_mid([6, 5, 4, 10, 2, 3, 9, 10])
