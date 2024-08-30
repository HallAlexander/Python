n, target = input().split(' ')
target = int(target)
lst = list(map(int, input().split()))
for i in range(int(n)):
    if lst[0] == target:
        print('fyrst')
        break
    elif lst[1] == target:
        print('naestfyrst')
        break
    elif lst[i] == target:
        print('{} fyrst'.format(i+1))