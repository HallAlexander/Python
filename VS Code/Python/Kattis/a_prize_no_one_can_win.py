num, price = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True)
while True:
    if len(nums) == 1:
        break
    elif nums[0] + nums[1] > price:
        nums.pop(0)
    else:
        break
print(len(nums))