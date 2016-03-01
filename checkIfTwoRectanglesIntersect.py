'''
Created on Feb 27, 2016

@author: bliu
'''


def checkIfTwoRectanglesIntersect(x1, y1, width1, length1, x2, y2, width2, length2):
    if (x1 + length1 >= x2 + length2 and x1 <= x2 + length2) or (x1 <= x2 and x1 + length1 >= x2):
        return True
    if (y1 + width1 >= y2 + width2 and y1 <= y2 + width2) or (y1 <= y2 and y1 + width1 >= y2):
        return True
    return False
        
        
if __name__ == '__main__':
    print checkIfTwoRectanglesIntersect(0, 0, 3, 6, 5, 5, 2, 2)
    