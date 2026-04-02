n = int(input())
first = True
while n != 0:
    matrix = []
    transform = {
    '-': '|',
    '|': '-',
    '+': '+'
    }
    for i in range(n):
        matrix.append(list(input()))
    max_len = max(len(row) for row in matrix)
    matrix = [row + [' '] * (max_len - len(row)) for row in matrix]
    rotated = list(zip(*matrix[::-1]))

    result = [
        ''.join(transform.get(c, c) for c in row)
        for row in rotated
    ]
    if not first:
        print()
    first = False
    
    print('\n'.join(row.rstrip() for row in result))
    n = int(input())