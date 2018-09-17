def charsmatch(elem):
    chars = {}
    for c in elem:
        chars[c] = 1
    return "".join(sorted("".join(chars.keys())))

def sort_and_group(x, groups):
    sorted_key = charsmatch(x)
    if (not sorted_key in groups):
        groups[sorted_key] = [x]
    else:
        groups[sorted_key].append(x)

def group_anagrams(anagram_input):
    groups = {}
    list(map(lambda x: sort_and_group(x, groups), anagram_input))
    res = []
    for k in groups:
        res.append(groups[k])
    return res

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

