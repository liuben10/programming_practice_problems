


def test_case_one():
    expected = "(((((((())))))))"
    actual = longest_valid_parenthesis("(((((((()))))))))))")
    if actual != expected:
        print("Expected = " + expected + ", " + "Actual=" + actual)
    else:
        print("longest_parens_passed")
        
def test_case_two():
    expected = "()()()()()"
    actual = longest_valid_parenthesis(")()()()()())")
    if actual != expected:
        print("Expected = " + expected + ", " + "Actual=" + actual)
    else:
        print("flat_parens_passed")

def longest_valid_parenthesis_at(parens, i):
    opens = 0
    max_substring = ""
    sub_so_far = ""
    for c in parens[i:]:
        if (opens == 0 and len(sub_so_far) > len(max_substring)):
            max_substring = sub_so_far
        if c == "(":
            opens += 1
        elif c == ")":
            if opens > 0:
                opens -= 1
            else:
                return max_substring
        sub_so_far += c
    return max_substring
            
                
def longest_valid_parenthesis(parens):
    hp = 0
    lp = 0
    max_so_far = ""
    for i in range(len(parens)):
        longest = longest_valid_parenthesis_at(parens, i)
        if (len(longest) > len(max_so_far)):
            max_so_far = longest
    return max_so_far
            
        

test_case_one()
test_case_two()
