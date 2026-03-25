n, *lst = map(int, input().split())

prefix_max = [0] * n
prefix_max[0] = lst[0]
for i in range(1, n):
    prefix_max[i] = max(prefix_max[i-1], lst[i])

suffix_min = [0] * n
suffix_min[-1] = lst[-1]
for i in range(n-2, -1, -1):
    suffix_min[i] = min(suffix_min[i+1], lst[i])

pivots = []
for i in range(n):
    left_ok = (i == 0 or lst[i] >= prefix_max[i-1])
    right_ok = (i == n-1 or lst[i] < suffix_min[i+1])
    
    if left_ok and right_ok:
        pivots.append(lst[i])

count = len(pivots)
print(count, end=' ')
print(*pivots[:100], end='')