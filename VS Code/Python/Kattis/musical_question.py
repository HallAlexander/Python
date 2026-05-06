def optim(lst, c):
    dp = [[False] * (c + 1) for _ in range(c + 1)]
    dp[0][0] = True
    for v in lst:
        for s1 in range(c, -1, -1):
            for s2 in range(c, -1, -1):
                if not dp[s1][s2]:
                    continue
                if s1 + v <= c:
                    dp[s1 + v][s2] = True
                if s2 + v <= c:
                    dp[s1][s2 + v] = True
    best_total = 0
    best_pair = (0, 0)
    for s1 in range(c + 1):
        for s2 in range(c + 1):
            if not dp[s1][s2]:
                continue
            total = s1 + s2
            if total > best_total or (
                total == best_total and abs(s1 - s2) < abs(best_pair[0] - best_pair[1])
            ):
                best_total = total
                best_pair = (s1, s2)
    return best_pair

c, n = map(int, input().split())
lst = list(map(int, input().split()))
ans = optim(lst, c)
print(ans[1], ans[0])