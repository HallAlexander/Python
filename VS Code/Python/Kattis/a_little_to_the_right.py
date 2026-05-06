n, m = map(int, input().split())
trophies = [list(map(int, input().split())) for _ in range(n)]
arrangements = 0
seen_orders = set()

for i in range(m):
    sorted_trophies = sorted(trophies, key=lambda x: x[i])
    col_vals = [row[i] for row in sorted_trophies]

    if all(col_vals[j] < col_vals[j + 1] for j in range(n-1)):
        order = tuple(tuple(row) for row in sorted_trophies)

        if order not in seen_orders:
            seen_orders.add(order)
            arrangements += 1
print(arrangements)