def closest_three_sum(elems, target):
    if (len(elems) < 3):
        return 0
    else:
        fp = 0
        sp = 1
        tp = 2
        closest = abs(target - elems[fp] + elems[sp] + elems[tp])
        closest_sum = elems[fp] + elems[sp] + elems[tp]
        
        while fp < sp:
            first = elems[fp]
            while sp < tp:
                sec = elems[sp]
                while tp < len(elems):
                    last = elems[tp]
                    old_closest = closest
                    closest = min(closest, abs(target - (first + sec + last)))
                    if (old_closest != closest):
                        closest_sum = first + sec + last
                    tp += 1
                sp += 1
            fp += 1

        return closest_sum
                    

print(closest_three_sum([-1, 2, 1, -4], 1))
