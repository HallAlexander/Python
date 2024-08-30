n = int(input())
if n % 2 == 1:
    print('Either')
elif (n / 2) % 2 == 1:
    print('Odd')
else:
    print('Even')
