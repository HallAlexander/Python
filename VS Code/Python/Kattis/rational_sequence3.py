
def get_fraction(goal):
    if goal == 1:
        return 1, 1
    p, q = 1, 1
    stack = []
    
    while goal > 1:
        if goal % 2 == 0:
            stack.append(True)  # even
        else:
            stack.append(False)  # odd
        goal //= 2
    
    while stack:
        if stack.pop():
            p, q = p, p + q
        else:
            p, q = p + q, q
    
    return p, q

runs = int(input())

for _ in range(runs):
    current_set, goal = map(int, input().split())
    result_p, result_q = get_fraction(goal)
    print(f"{current_set} {result_p}/{result_q}")
