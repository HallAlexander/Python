length = int(input())
roads = int(input())
total_spaces = 0
empty_spaces = 0
for i in range(roads):
    string = input()
    total_spaces += len(string)
    for c in string:
        if c == '.':
            empty_spaces += 1
print(empty_spaces/total_spaces)
