n, req = input().split(' ')
res = 0
for i in range(int(n)):
    res += int(input())
if res <= int(req):
    print('Jebb')
else:
    print('Neibb')
    