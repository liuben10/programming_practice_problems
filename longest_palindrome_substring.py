"""
babad
longest = aba

bb

longest = bb
"""
def longest_palindrome_substring(word):
    if not len(word):
        return word
    longest_indices = []
    max_len = 0
    for i in range(len(word)):
        hp = i
        lp = i
        while lp >= 0 and hp < len(word) and word[lp] == word[hp]:
            if hp - lp + 1 > max_len:
                max_len = hp - lp + 1
                longest_indices = [lp, hp]
            lp -= 1
            hp += 1
            

        hp = i
        lp = i-1
        while lp >= 0 and hp < len(word) and word[lp] == word[hp]:
            if hp - lp + 1 > max_len:
                max_len = hp - lp + 1
                longest_indices = [lp, hp]
            lp -= 1
            hp += 1
    return word[longest_indices[0]:longest_indices[1]+1]

print(longest_palindrome_substring("b"))
