'''
Created on Jan 28, 2016

@author: bliu
'''


def permutation(input):
    print "input=" + input
    if (len(input) == 1):
        return [input[0]]
    reslist = []
    for i in range(len(input)):
        curchar = input[i]
        print curchar
        new_input = input[:i] + input[i+1:]
        results = permutation(new_input)
        for res in results:
            reslist.append(curchar + res)
    return reslist

def to_binary_string(decimal):
    n = decimal
    res = ""
    while n > 0:
        res = str(n % 2) + res
        n /= 2
    return res

def combination(input):
    n = len(input)
    flip_board = []
    results = []
    for i in range(pow(2, n)):
        flip_board.append(to_binary_string(i).zfill(n))
    print flip_board
    for flip in flip_board:
        combo_str = ""
        for i in range(len(flip)):
            if (flip[i] == "1"):
                combo_str += input[i]
        results.append(combo_str)
    return results

if __name__ == '__main__':
    print combination("abcdefg")