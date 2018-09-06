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


print(longest_substring_without_repeating("aabbbcdf"))
            
