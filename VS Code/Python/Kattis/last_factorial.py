import math
n = int(input())
result = []
for i in range(n):
    number = int(input())
    number = math.factorial(number)
    if number > 10:
        number %= 10
    result.append(number)
for x in result:
    print(x)