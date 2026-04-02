from math import sqrt
smallest = int(input())
papers = list(map(int, input().split()))
len = 2**-(3/4)

tape = 0
required = 1
for paper in papers:
    required *=2
    tape += (required//2) * len
    required -= paper
    if required <= 0:
        break
    len /= sqrt(2)
if required <= 0:
    print(tape)
else:
    print('impossible')
