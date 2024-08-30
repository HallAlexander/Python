runs = int(input())

string = input()
lst = [x for x in string]
possible_move = True
for i in range(len(lst)):
    if lst[i] == 'o' and lst[i-2] == 'o' and lst[i-1] == '-':
        