n = int(input())
counts = {'STU':0, 'FAC':0, 'VIS':0}
for _ in range(n):
    rank, state, num = input().split()
    if state == 'IN':
        counts[rank] += int(num)
    else:
        counts[rank] -= int(num)

if sum(counts.values()) == 0:
    print('NO STRAGGLERS')
else:
    print(sum(counts.values()))