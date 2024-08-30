def always_up(lst, init):
    counter = 0
    previous_seat = init
    for i in range(len(lst)):
        if lst[i] != previous_seat and lst[i] != 'U':
            counter += 2
        elif lst[i] != previous_seat and lst[i] == 'U':
            counter += 1
        elif lst[i] == previous_seat and lst[i] != 'U':
            counter += 1

        previous_seat = 'U' 
    print(counter)

def always_down(lst, init):
    counter = 0
    previous_seat = init
    for i in range(len(lst)):
        if lst[i] != previous_seat and lst[i] != 'D':
            counter += 2
        elif lst[i] != previous_seat and lst[i] == 'D':
            counter += 1
        elif lst[i] == previous_seat and lst[i] != 'D':
            counter += 1
        previous_seat = 'D'
    print(counter)

def prefered(lst, init):
    counter = 0
    previous_seat = init
    for i in range(len(lst)):
        if lst[i] != previous_seat:
            counter += 1
        previous_seat = lst[i]
    print(counter)

lst = list(input())
initial = lst.pop(0)
always_up(lst, initial)
always_down(lst, initial)
prefered(lst, initial)
