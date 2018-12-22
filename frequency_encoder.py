def frequency_encode(s):
    i = 0
    count = 1
    cur = s[0]
    prev = s[0]
    encoded = ""
    while i < len(s):
        i += 1
        if (i >= len(s)):
            break
        cur = s[i]
        if (cur == prev):
            count += 1
        else:
            encoded += prev + str(count)
            count = 1
        prev = cur
    encoded += prev + str(count)
    return encoded

print(frequency_encode("aaabbbcccccdd"))
