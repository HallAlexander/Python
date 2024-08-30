lst = input().split(' ')
for i in range(len(lst)):
    lst[i] = int(lst[i])
bob_money = ((lst[1] - lst[0]) * lst[2])
alice_money = lst[4]
lst[3] += 1
while(alice_money <= bob_money):
    alice_money += lst[4]
    lst[3] += 1
print(lst[3])