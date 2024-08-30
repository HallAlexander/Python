items, mark = input().split(' ')
items = int(items)
if(items == 1):
    print(1)
else:
    mark = int(mark)
    data = input().split(' ')
    for i in range(len(data)):
        data[i] = int(data[i])
    data.sort()
