'''
Created on Feb 20, 2016

@author: bliu
'''


def combination(str):
    result = []
    for i in range(len(str)+1):
        comboCore(str, 0, i, result)

def comboCore(str, index, number, result):
    if number == 0:
        print(result)
    if (index == len(str)):
        return
    result.append(str[index])
    comboCore(str, index+1, number-1, result)
    result.pop()
    comboCore(str, index+1, number, result)
    
if __name__ == '__main__':
    comboCore("foobar", 0, 2, [])