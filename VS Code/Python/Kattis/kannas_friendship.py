import bisect

intervals = []
total = 0

def add_interval(L, R):
    global total
    
    i = bisect.bisect_left(intervals, (L, R))
    if i > 0 and intervals[i-1][1] >= L - 1:
        i -= 1
    new_L, new_R = L, R
    to_remove = []
    while i < len(intervals) and intervals[i][0] <= R + 1:
        l, r = intervals[i]
        new_L = min(new_L, l)
        new_R = max(new_R, r)
        total -= (r - l + 1)
        to_remove.append(i)
        i += 1
    for idx in reversed(to_remove):
        intervals.pop(idx)
    bisect.insort(intervals, (new_L, new_R))
    total += (new_R - new_L + 1)

n, q = map(int, input().split())
for _ in range(q):
    s = input()
    if ' ' in s:
        cmd, l, r = map(int, s.split())
        if cmd == 1:
            add_interval(l, r)
    else:
        print(total)