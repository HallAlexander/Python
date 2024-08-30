potions, drinking_time = input().split(' ')
potions = int(potions)
drinking_time = int(drinking_time)
pot_list = []
for i in range(potions):
    pot_list.append(int(input()))
pot_list.sort(reverse = True)
tot = (potions-1) * drinking_time
if(tot < pot_list[0]):
    print('YES')
else:
    print('NO')