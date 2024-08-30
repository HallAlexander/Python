parts, purchases = input().split(' ')
parts = int(parts)
purchases = int(purchases)
day = 1
lst = []
for i in range(purchases):
    part = input()
    if part not in lst:
        lst.append(part)
        parts -= 1
    if parts == 0:
        break
    day += 1
if parts != 0:
    print('paradox avoided')
else:
    print(day)
    