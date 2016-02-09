'''
Created on Jan 31, 2016

@author: bliu
'''


def check_if_paren_balance(input_str):
    stack = []
    if (input_str is None or input_str is ""):
        return True
    for character in input_str:
        if character is "(":
            stack.append(character)
        elif character is ")":
            if (len(stack) > 0 and stack[len(stack)-1] is "("):
                stack.pop()
            else:
                return False
    if not stack:
        return True
    return False

if __name__ == '__main__':
    print check_if_paren_balance("((()))")