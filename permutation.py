'''
Created on Jan 28, 2016

@author: bliu
'''


def permutation(input):  # @ReservedAssignment
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


def combination(input):  # @ReservedAssignment
    n = len(input)
    results = []
    for i in range(pow(2, n)):
        combo_str = ""
        flip = to_binary_string(i)[::-1]
        for i in range(len(flip)):
            if (flip[i] == "1"):
                combo_str += input[i]
        results.append(combo_str)
    return results

if __name__ == '__main__':
    print combination("abcdefg")