def find_in_list(sorted_arr, target):
    lp = 0
    hp = len(sorted_arr) - 1
    if (len(sorted_arr) == 1):
        0 if target == sorted_arr[0] else -1
    while lp < hp:
        mp = (hp + lp) // 2
        if (sorted_arr[mp] == target):
            return mp
        else:
            if target > sorted_arr[mp]:
                lp = mp+1
            else:
                hp = mp
    return -1

def find_tail(sorted_arr, found_idx, target):
    lp = 0
    hp = found_idx
    while(lp < hp):
        mp = (hp + lp) // 2
        if (mp == 0 and sorted_arr[mp] == target):
            return 0
        elif (mp == found_idx):
            return found_idx
        elif (sorted_arr[mp] == target and sorted_arr[mp-1] != target):
            return mp
        else:
            if sorted_arr[mp] != target:
                lp = mp+1
            else:
                hp = mp
    return -1

def find_head(sorted_arr, found_idx, target):
    lp = found_idx
    hp = len(sorted_arr) - 1
    while(lp < hp):
        mp = (hp + lp) // 2
        if (mp == len(sorted_arr) - 1 and sorted_arr[mp] == target):
            return len(sorted_arr) - 1
        elif (mp == found_idx):
            return found_idx
        elif (sorted_arr[mp] == target and sorted_arr[mp+1] != target):
            return mp
        else:
            if sorted_arr[mp] != target:
                lp = mp+1
            else:
                hp = mp
    return -1
    
    
def find_first_and_last(sorted_arr, target):
    found_idx = find_in_list(sorted_arr, target)
    if (found_idx == -1):
        return [-1, -1]
    tail = find_tail(sorted_arr, found_idx, target)
    head = find_head(sorted_arr, found_idx, target)
    return [tail, head]



print(find_first_and_last([5,7,7,8,8,10], 8))
