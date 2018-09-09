def largest_bounded_rect(histogram):
    if (len(histogram) == 1):
        return histogram[0]
    midpoint = len(histogram) // 2
    vol = vol_in_range(histogram, midpoint)
    left_vol = largest_bounded_rect(histogram[0:midpoint])
    right_vol = largest_bounded_rect(histogram[midpoint:])
    return max(left_vol, right_vol, vol)

def vol_in_range(histogram, mid):
    print("histogram=%s, mid=%d" % (histogram, mid))
    lp = mid
    hp = mid+1
    if (hp >= len(histogram)):
        return histogram[0]
    largest_volume = 0
    height = min(histogram[lp], histogram[hp])
    while(lp >= 0 and hp < len(histogram)):
        print("lp=%d, hp=%d" % (lp, hp))
        height = min(height, min(histogram[lp], histogram[hp]))
        largest_volume = max(largest_volume, (hp - lp + 1) * height)
        if (lp == 0):
            hp += 1
        elif (hp == len(histogram) - 1):
            lp -= 1
        else:
            if (histogram[hp] > histogram[lp]):
                hp += 1
            else:
                lp -= 1
    return largest_volume

def largest_area_bounded_stack(histogram):
    stack = []
    max_vol = 0
    height=0
    for i, elem in enumerate(histogram):
        print(stack)
        if (not stack or elem >= histogram[stack[0]]):
            stack.insert(0, i)
        else:
            while (stack and histogram[stack[0]] > elem):
                height = i if not stack else i - stack[0]
                print("h=%d" % height)
                max_vol = max(max_vol, (height) * histogram[stack[0]])
                stack = stack[1:]
            stack.insert(0, i)

    while (stack):
        max_vol = max(max_vol, (len(histogram) - stack[0]) * histogram[stack[0]])
        stack = stack[1:]
    return max_vol
            
            
                
            
print(largest_bounded_rect([5, 10, 9]))
print(largest_area_bounded_stack([5, 10, 9]))



print(largest_bounded_rect([12, 14, 3]))
print(largest_area_bounded_stack([12, 14, 3]))
