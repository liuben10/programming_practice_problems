def histogram_vol(histo):
    maxes_from_left = []
    maxLeft = float('-inf')
    for elem in histo:
        if (elem > maxLeft):
            maxLeft = elem
        maxes_from_left.append(maxLeft)

    maxes_from_right = []
    maxRight = float('-inf')
    for elem in histo[::-1]:
        if (elem > maxRight):
            maxRight = elem
        maxes_from_right.append(maxRight)

    maxes_from_right = maxes_from_right[::-1]

    volume = 0
    for i in range(len(histo)):
        tallest = min(maxes_from_left[i], maxes_from_right[i])
        volume += (tallest - histo[i])

    return volume


print(histogram_vol([5, 1, 2, 4]))
