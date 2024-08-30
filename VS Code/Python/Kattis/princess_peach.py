obstacles, found = input().split(' ')
lst = []
for i in range(int(found)):
    lst.append(int(input()))
lst = list(dict.fromkeys(lst))
iterator = 0
found_check = False
for i in range(int(obstacles)):
    for j in range(len(lst)):
        if iterator == lst[j]:
            found_check = True
    if(found_check == True):
        found_check = False
        iterator += 1
    else:
        print(iterator)
        iterator += 1
print('Mario got ' + str(len(lst)) + ' of the dangerous obstacles.')