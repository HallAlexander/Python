integer = int(input())
counter = 1
while integer > 9:
    integer /= 9
    print(integer)
    counter += 1
if counter % 2 == 1:
    print('Stan wins.')
else:
    print('Ollie wins.')