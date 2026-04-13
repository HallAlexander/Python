nums = list(map(int, input().split()))
nums.sort()
maps = {
    'A':0,
    'B':1,
    'C':2
}
order = input()
out = []
for c in order:
    out.append(nums[maps[c]])
print(*out)