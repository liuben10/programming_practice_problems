'''
Created on Jan 31, 2016

@author: bliu
'''


def can_sit(chair, distance, result):
    for occupied in result:
        if chair < occupied + distance and chair > occupied - distance:
            return False
    return True
        


def bear_chair(chairs, distance):
    result = []
    for chair in chairs:
        if (can_sit(chair, distance, result)):
            result.append(chair)
        else:
            new_chair = chair
            while( not can_sit(new_chair, distance, result)):
                new_chair += 1
            result.append(new_chair)
    return result

if __name__ == '__main__':
    print bear_chair([1000000,1000000,1000000,1], 1000000)