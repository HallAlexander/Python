print(*[-(x + y) for x, y in zip([int(x) for x in input().split(' ')], [-1, -1, -2, -2, -2, -8])], sep=' ')

"""in = [int(x) for x in input().split(' ')]
lst = [-1, -1, -2, -2, -2, -8]
res = [x + y for x, y in zip(in, lst)]
res = -res
print(*res, sep=' ')
"""
