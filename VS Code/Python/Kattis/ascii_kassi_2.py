n = int(input())
for _ in range(n+1):
    print(' ', end='')
print('x')
n2 = n
inner = 1
while n2 > 0:
    for _ in range(n2):
        print(' ', end='')
    print('/', end='')
    for _ in range(inner):
        print(' ', end='')
    print('\\')
    n2 -= 1 
    inner += 2
print('x', end='')
for _ in range(inner):
    print(' ', end='')
print('x')
inner -= 2
n2 += 1
while n2 <= n:
    for _ in range(n2):
        print(' ', end='')
    print('\\', end='')
    for _ in range(inner):
        print(' ', end='')
    print('/')
    n2 += 1 
    inner -= 2
for _ in range(n+1):
    print(' ', end='')
print('x')