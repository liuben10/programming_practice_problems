def longest_substring_without_repeating(substr):
    repeats = 0
    prev = None
    run = {}
    longestSoFar = 0
    for c in substr:
        if (prev == None):
            prev = c
            run[c] = 1
        else:
            runlen = len(run)
            if (prev == c):
                if runlen > longestSoFar:
                    longestSoFar = runlen
                run = {}
                run[c] = 1
            else:
                run[c] = 1
            prev = c

    runlen = len(run)
    if (runlen > longestSoFar):
        longestSoFar = runlen
    return longestSoFar

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    max_substr_len = float('-inf')
    for i in range(len(s)):
        wcs = {}
        for j in range(i, len(s)):
            if (s[j] in wcs):
                max_substr_len = max(len(wcs), max_substr_len)
                wcs = {}
                break
            else:
                wcs[s[j]] = ''
        if len(wcs):
            max_substr_len = max(len(wcs), max_substr_len)
        
    return max_substr_len
            

print(longest_substring_without_repeating("aabbbcdf"))
print(lengthOfLongestSubstring("abcabcbb"))
            
