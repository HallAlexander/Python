n, m = input().split(' ')
day1 = input().split(' ')
day2 = input().split(' ')
n = int(n)
m = int(m)
day1 = [int(x) for x in day1]
day2 = [int(x) for x in day2]
result = []
for i in range(n):
    for j in range(m):
        if day2[j] == day1[i]:
            result.append(day2[j])
for i in range(len(result)):
    print(result[i], end=' ')
