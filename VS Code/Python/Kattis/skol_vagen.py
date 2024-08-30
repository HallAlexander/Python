string = input()
north, south = [], []

for c in string:
    if c == 'N':
        north.append(1)
        south.append(0)
    elif c == 'S':
        north.append(0)
        south.append(1)
    elif c == 'B':
        north.append(1)
        south.append(1)
print(north)
print(south)