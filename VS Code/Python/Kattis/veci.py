def permute(nums):
    result = [[]]
    num_result = []
    for n in nums:
        new_permutation = []
        for perm in result:
            for i in range(len(perm) + 1):
                new_permutation.append(perm[:i] + [n] + perm[i:])
        result = new_permutation
    for x in result:
        num_result.append(int(''.join([str(n) for n in x])))
    num_result.sort()
    return(num_result)
  
num = input()
lst = [*num]
num = int(num)
lst = [int(x) for x in lst]
lst = permute(lst)
result = 0
for x in lst:
    if x > num:
        result = x
        break
print(result)
