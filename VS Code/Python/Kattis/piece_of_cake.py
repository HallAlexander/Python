n, h, v = input().split(' ')
n = int(n)
h = int(h)
v = int(v)
if n - h <= h:
    result = 4 * h
else:
    result = 4 * (n - h)
if n - v <= v:
    result *= v
else:
    result *= (n - v)
print(result)