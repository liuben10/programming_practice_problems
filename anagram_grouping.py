def anagrams(ungrouped):
    result = {}
    for e in ungrouped:
        key = ''.join(sorted(e))
        if key in result:
            result[key].append(e)
        else:
            result[key] = [e]

            
    reslist = []
    for k in result:
        reslist.append(result[k])
    return reslist
    



test_in = [
    "aet",
    "bat",
    "tea",
    "abt",
    "bbt"
]

print(anagrams(test_in))
