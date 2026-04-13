from collections import defaultdict
t = int(input())
for ct in range(1, t+1):
    n, a, b, c, d, x0, y0, m = map(int, input().split())
    coords = []
    x = x0
    y = y0
    coords.append((x, y))
    for i in range(1, n):
        x = (a*x + b) % m
        y = (c*y + d) % m
        coords.append((x, y))

    cnt = defaultdict(int)
    for x, y in coords:
        cnt[(x % 3, y % 3)] += 1
    ans = 0
    groups = list(cnt.keys())
    for i in range(len(groups)):
        for j in range(i, len(groups)):
            for k in range(j, len(groups)):
                g1, g2, g3 = groups[i], groups[j], groups[k]

                if (g1[0] + g2[0] + g3[0]) % 3 != 0:
                    continue
                if (g1[1] + g2[1] + g3[1]) % 3 != 0:
                    continue

                c1, c2, c3 = cnt[g1], cnt[g2], cnt[g3]

                if i == j == k:
                    ans += c1 * (c1 - 1) * (c1 - 2) // 6
                elif i == j:
                    ans += c1 * (c1 - 1) // 2 * c3
                elif j == k:
                    ans += c2 * (c2 - 1) // 2 * c1
                else:
                    ans += c1 * c2 * c3
    print(f"Case #{ct}: {ans}")