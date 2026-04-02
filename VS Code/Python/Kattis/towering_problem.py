from itertools import combinations

*lst, h1, h2 = map(int, input().split())
lst.sort(reverse=True)

for comb in combinations(lst, 3):
    if sum(comb) == h1:
        remaining = lst.copy()
        for x in comb:
            remaining.remove(x)

        if sum(remaining) == h2:
            print(*comb, *remaining)
            break
