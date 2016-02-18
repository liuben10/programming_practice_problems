'''
Created on Feb 8, 2016

@author: bliu
'''

def print_in_spiral(input_matrix):
    start = 0
    xlen = len(input_matrix[0])
    ylen = len(input_matrix)
    while (start * 2 < xlen and start * 2 < ylen ):
        print_leg(input_matrix, start, start)
        start += 1
    
def print_leg(input_matrix, start_x, start_y):
    rowlen = len(input_matrix[0])
    collen = len(input_matrix)
    endx = rowlen - start_x
    endy = collen - start_y
    for topx in range(start_x, endx):
        print input_matrix[start_y][topx]
    for righty in range(start_y+1, endy):
        print input_matrix[righty][endx-1]
    for botx in range(endx-2, start_x, -1):
        print input_matrix[endy-1][botx]
    for lefty in range(endy - 1, start_y, -1):
        print input_matrix[lefty][start_x]

if __name__ == '__main__':
    print_in_spiral([[1, 2, 3, 11], [4, 5, 6, 12], [7, 8, 9, 13], [14, 15, 16, 17]])