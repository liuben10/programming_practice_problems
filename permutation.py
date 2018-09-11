'''
Created on Jan 28, 2016

@author: bliu
'''


def permutation(testin):   
    print("testin=" + testin)
    if (len(testin) == 1):
        return [testin[0]]
    reslist = []
    for i in range(len(testin)):
        curchar = testin[i]
        print(curchar)
        new_testin = testin[:i] + testin[i+1:]
        results = permutation(new_testin)
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


def combination(testin):
    n = len(testin)
    results = []
    for i in range(pow(2, n)):
        combo_str = ""
        flip = to_binary_string(i)[::-1]
        for i in range(len(flip)):
            if (flip[i] == "1"):
                combo_str += testin[i]
        results.append(combo_str)
    return results

def combination_recursive(test_in):
    if (len(test_in) == 1):
        return test_in[0]
    cur = test_in[0]
    result = []
    combinations = combination_recursive(test_in[1:])
    for combo in combinations:
        for j in range(len(combo)):
            result.append(combo[:j] + cur + combo[j:len(combo)])
    return result
            
        

if __name__ == '__main__':
    print(combination_recursive("abcdefg"))
