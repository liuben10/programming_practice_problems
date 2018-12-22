def find_all_repeats(s):
    window_set = {}
    repeats = {}
    if (len(s) < 10):
        return []
    window_end = 10
    window_start = 0
    window_set[s[window_start:window_end]] = 1
    while window_end < len(s):
        window_end += 1
        window_start += 1
        
        window = s[window_start:window_end]
        if window in window_set:
            repeats[window] = 1
        else:
            window_set[window] = 1
    return list(repeats.keys())
    
all_repeats = find_all_repeats("AAAAAAAAAAA")
print(all_repeats)
