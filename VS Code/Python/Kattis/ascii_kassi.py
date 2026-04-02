n = int(input())
print('+', end='')
for _ in range(n):
    print('-', end='')
print('+')
for _ in range(n):
    print('|', end='')
    for _ in range(n):
        print(' ', end='')
    print('|')
print('+', end='')
for _ in range(n):
    print('-', end='')
print('+')