count = 0
y_count = 0
for c in input():
    if c in 'aeiou':
        count += 1
    if c in 'aeiouy':
        y_count += 1
print('{} {}'.format(count, y_count))
