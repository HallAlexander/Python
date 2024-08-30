strlst = input().split(' ')
intlst = []
for i in range(len(strlst)):
    if strlst[i] == 'South':
        intlst.append(0)
    elif strlst[i] == 'East':
        intlst.append(1)
    elif strlst[i] == 'North':
        intlst.append(2)    
    elif strlst[i] == 'West':
        intlst.append(3)

if (intlst[0] + 1 ) % 4 == intlst[1]:
    print('No')
elif (intlst[0] + 1) % 4 == intlst[2]:
    print('Yes')
elif (intlst[0] + 3) % 4 == intlst[1] and (((intlst[0] + 2) % 4 == intlst[2]) or ((intlst[0] + 1) % 4 == intlst[2])):
    print('Yes')
else:
    print('No')