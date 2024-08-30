sides = input().split(' ')
sides = [int(x) for x in sides]
while(sides != [0, 0, 0]):
    sides.sort()
    if((pow(sides[0], 2) + pow(sides[1], 2)) == pow(sides[2],2)):
        print('right')
    else:
        print('wrong')
    sides = input().split(' ')
    sides = [int(x) for x in sides]
