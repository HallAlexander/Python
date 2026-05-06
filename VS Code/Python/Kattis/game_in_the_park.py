n = int(input())
board = [list(map(int, input().split())) for _ in range(4)]

valid_masks = []
for mask in range(1 << 4):
    if (mask & (mask << 1)) == 0:
        valid_masks.append(mask)
col_score = []
for col in range(n):
    scores = {}
    for mask in valid_masks:
        total = 0
        for row in range(4):
            if mask & (1 << row):
                total += board[row][col]
        scores[mask] = total
    col_score.append(scores)
dp = {mask: 0 for mask in valid_masks}
for col in range(n):
    new_dp = {mask: float('-inf') for mask in valid_masks}
    for curr_mask in valid_masks:
        for prev_mask in valid_masks:
            if curr_mask & prev_mask == 0:
                new_dp[curr_mask] = max(
                    new_dp[curr_mask],
                    dp[prev_mask] + col_score[col][curr_mask]
                )
    dp = new_dp
print(max(dp.values()))