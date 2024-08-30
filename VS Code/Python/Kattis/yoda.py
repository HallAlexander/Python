list1 = [x for x in input()]
list2 = [x for x in input()]

while len(list1) > len(list2):
    list2.insert(0, '')
while len(list2) > len(list1):
    list1.insert(0, '')

for i in range(len(list1)):
    if list1[i] == '' or list2[i] == '':
        continue
    elif int(list1[i]) > int(list2[i]):
        list2[i] = ''
    elif int(list2[i]) > int(list1[i]):
        list1[i] = ''

if all([x == '' for x in list1]):
    print('YODA')
else:
    int1 = int(''.join(list1))
    print(int1)
if all([x == '' for x in list2]):
    print('YODA')
else:
    int2 = int(''.join(list2))
    print(int2)
