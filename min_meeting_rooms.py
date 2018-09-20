def min_meeting_rooms(intervals):
    N = len(intervals)
    if (N == 0):
        return 0
    sorted_by_starts = [s for s in sorted(intervals, key=lambda x: x[0])]
    print(sorted_by_starts)
    sp = 0
    ep = 0
    num_rooms = 1
    free_rooms = 0
    while ep < N and sp < N:
        interval = sorted_by_starts[ep]
        if (interval[0] >= sorted_by_starts[sp][0]\
            and interval[0] <= sorted_by_starts[sp][1]):
            if (sp != ep):
                if (free_rooms):
                    free_rooms -= 1
                else:
                    num_rooms += 1
            ep += 1
        else:
            free_rooms += 1
            sp += 1
    return num_rooms

print(min_meeting_rooms([[1, 4], [3, 9], [11, 13]]))
print(min_meeting_rooms([[2, 5], [3, 7], [6, 10]]))
print(min_meeting_rooms([[1,20], [2, 19], [3, 15], [4, 16]]))
print(min_meeting_rooms([[2, 10], [3, 16], [11, 19]]))
