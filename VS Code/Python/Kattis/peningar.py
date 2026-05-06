n, d = map(int, input().split())
lst = list(map(int, input().split()))

summ = 0
i = 0
while(True):
    if lst[i] != 0:
        summ += lst[i]
        lst[i] = 0
        i += d
        i %= len(lst)
    else:
        break
print(summ)