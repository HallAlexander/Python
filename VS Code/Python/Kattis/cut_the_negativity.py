n = int(input())
flights = []
for i in range(n):
    row = input().split(' ')
    row = [int(x) for x in row]
    for j in range(len(row)):
        if row[j] != -1:
            flights.append([i + 1, j + 1, row[j]])
print(len(flights))
for x in flights:
    for i in range(len(x)):
        print(x[i], end=' ')
    print()