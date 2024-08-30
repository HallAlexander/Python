n = int(input())
lst = {}
for i in range(n):
    name, score = input().split(' ')
    lst.update({name: int(score)})
print(list(dict(sorted(lst.items(), key=lambda x:x[1], reverse=True)).keys())[0])
