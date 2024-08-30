n = int(input())
lst = []
for i in range(n):
    lst.append(input())
lst.sort()
nums = []
counter = 1
for i in range(1, len(lst)):
    if(lst[i - 1] == lst[i]):
        counter += 1
    else:
        nums.append(counter)
        counter = 1
nums.append(counter)
lst = list(set(lst))
lst.sort()
tmpnums = sorted(nums)
if(tmpnums.count(tmpnums[0]) > 1):
    for i in range(len(nums)):
        if(nums[i] == tmpnums[0]):
            print(lst[i])
else:
    print(lst[nums.index(tmpnums[0])])
