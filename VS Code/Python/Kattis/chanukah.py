runs = int(input())
while runs > 0:
    run, days = input().split(' ')
    days = int(days)
    sum = days
    while days > 0:
        sum += days
        days -= 1
    print('{} {}'.format(int(run), sum))
    runs -= 1
    