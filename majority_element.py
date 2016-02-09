'''
Created on Dec 26, 2015

@author: bliu
'''

def majority_element(input):
    counts = {}
    for elem in input:
        if (counts.has_key(elem)):
            counts[elem] += 1
            if (counts[elem] >= len(input) / 2):
                return elem
        else:
            counts[elem] = 1
    return -1

    
    

if __name__ == '__main__':
    print majority_element([1, 2, 3, 2, 2, 4])