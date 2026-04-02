input()
left = sum(list(map(int, input().split())))
right= sum(list(map(int, input().split())))
if left < right:
    print('left')
elif right < left:
    print('right')
else:
    print('either')