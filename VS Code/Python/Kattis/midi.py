n = int(input())
lst = []
for i in range(n):
    lst.append(input()[::-1])
lst = lst[::-1]
for x in lst:
    print(x, end='')