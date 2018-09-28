def match(input_str, pattern):
    pidx = 0
    iidx = 0
    while (iidx < len(input_str) and pidx < len(pattern)):
        pcur = pattern[pidx]
        if pcur == "*":
            if len(pattern) == 1:
                return True
            else:
                next_p = pattern[pidx+1]
                seq_idx = iidx
                while input_str[seq_idx] != next_p:
                    seq_idx += 1
                return match(input_str[seq_idx:], pattern[pidx+1:])
        elif pcur == "?":
            pidx += 1
            iidx += 1
        else:
            if pcur != input_str[iidx]:
                return False
            else:
                pidx += 1
                iidx += 1

    return True
                    
        
    

print(match("aa", "*"))
print(match("cb", "?a"))
print(match("adceb", "*a*b"))
print(match("acdcb", "a*c?b"))
