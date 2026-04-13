MOD = 1000000007

def optimal_huge(n, t, a, b, c, t0):
    pos = [-1] * (c + 1)
    order = []
    cur = t0
    step = 0
    while pos[cur] == -1:
        pos[cur] = step
        order.append(cur)
        step += 1
        cur = ((a * cur + b) % c) + 1

    cycle_start = pos[cur]
    prefix = order[:cycle_start]
    cycle = order[cycle_start:]
    freq = [0] * (c + 1)
    for x in prefix:
        freq[x] += 1
    
    remaining_n = n - len(prefix)
    if remaining_n > 0:
        cycle_len = len(cycle)
        cycle_freq = [0] * (c + 1)
        for x in cycle:
            cycle_freq[x] += 1
        full_cycles = remaining_n // cycle_len
        remainder = remaining_n % cycle_len
        for x in range(1, c + 1):
            freq[x] += cycle_freq[x] * full_cycles
        for i in range(remainder):
            freq[cycle[i]] += 1

    total_time = 0
    solved = 0
    penalty = 0

    for x in range(1, c + 1):
        count = freq[x]
        if count == 0:
            continue
        remaining = t - total_time
        if remaining < x:
            break
        k = min(count, remaining // x)
        penalty = (penalty + k * total_time) % MOD
        penalty = (penalty + x * (k * (k + 1) // 2)) % MOD
        total_time += k * x
        solved += k
    return solved, penalty

n,t = map(int,input().split())
a,b,c,t0 = map(int,input().split())
print(*optimal_huge(n, t, a, b, c, t0))