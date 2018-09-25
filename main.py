

def max_rect(histo):
    stack = []
    max_rect = 0
    for i, e in enumerate(histo):
        if (len(stack) == 0 or (e > histo[stack[0]])):
            stack.insert(0, i)
        else:
            while (stack and e < histo[stack[0]]):
                topIdx = stack[0]
                top = histo[stack.pop(0)]
                max_rect = max(top * (i - topIdx), max_rect)

    while (stack and e < histo[stack[0]]):
        topIdx = stack[0]
        top = histo[stack.pop(0)]
        max_rect = max(top * (i - topIdx), max_rect)
    return max_rect

        
print(max_rect([9, 10, 11, 5, 19, 13]))
