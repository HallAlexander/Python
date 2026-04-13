def count_subsequence(s, pattern):
    dp = [0] * (len(pattern) + 1)
    dp[0] = 1
    for ch in s:
        for i in range(len(pattern) - 1, -1, -1):
            if ch == pattern[i]:
                dp[i + 1] += dp[i]
    return dp[len(pattern)]
message = 'welcome to code jam'

for i in range(1, int(input())+1):
    print(f"Case #{i}: {count_subsequence(input(), message) % 10000:04d}")