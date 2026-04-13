def build_arrays(s):
    from collections import defaultdict, deque
    groups = defaultdict(deque)
    arrays = []
    result = []
    for ch in s:
        placed = False
        for size in [2, 1, 0]:
            for state in list(groups.keys()):
                if len(state) == size and ch not in state:
                    idx = groups[state].popleft()
                    if not groups[state]:
                        del groups[state]

                    new_state = set(state)
                    new_state.add(ch)

                    result[idx].append(ch)

                    if len(new_state) == 3:
                        new_state = set()

                    new_state = frozenset(new_state)
                    groups[new_state].append(idx)
                    arrays[idx] = new_state

                    placed = True
                    break
            if placed:
                break
        if not placed:
            idx = len(arrays)
            arrays.append(frozenset([ch]))
            result.append([ch])
            groups[frozenset([ch])].append(idx)
    for r in result:
        if len(r) % 3 != 0:
            return None
    return result
print(len(build_arrays(input())))