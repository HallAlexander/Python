string = input()
lst = []

for c in string:
    if c == '<':
        if lst:
            lst.pop()
    else:
        lst.append(c)
res = ''.join(lst)
print(res)