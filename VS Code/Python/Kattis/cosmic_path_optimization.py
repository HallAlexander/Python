import math
input()
lst = list(map(int, input().split()))
mean = 0
for x in lst:
    mean += x
print(math.floor(mean / len(lst)))
