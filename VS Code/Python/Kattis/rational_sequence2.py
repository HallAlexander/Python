def find_goal(p, q):
    goal = 1
    while (p, q) != (1, 1):
        if p > q:
            p -= q
            goal = goal * 2 + 1
        else:
            q -= p
            goal = goal * 2
    return goal

runs = int(input())

for _ in range(runs):
    current_set, fraction = input().split()
    p, q = map(int, fraction.split('/'))
    goal = find_goal(p, q)
    print(f"{current_set} {goal}")
