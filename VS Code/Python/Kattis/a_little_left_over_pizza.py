pizzas = int(input())
s, m, l = 0, 0, 0
for i in range(pizzas):
    type, num = input().split(' ')
    if type == 'S':
        s += int(num)
    elif type == 'M':
        m += int(num)
    elif type == 'L':
        l += int(num)
s = int(s/6) + (s % 6 > 0) 
m = int(m/8) + (m % 8 > 0)
l = int(l/12) + (l % 12 > 0)
print(s + m + l)