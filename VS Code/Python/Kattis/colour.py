socks, socks_per_machine, colour_diff = input().split(' ')
socks = int(socks)
socks_per_machine = int(socks_per_machine)
colour_diff = int(colour_diff)

socks_lst = list(map(int, input().split()))
socks_lst.sort()
machines = []
for i in range(socks_per_machine):
    if socks_per_machine * i < socks + socks_per_machine:
        machines.append(0)

machine_counter = 0
for i in range(len(socks_lst)):
    
    if i == 0:
        machines[machine_counter] += 1
    elif socks_lst[i] == socks_lst[i - 1]:
        if machines[machine_counter] < socks_per_machine:
            machines[machine_counter] += 1
        else:
            machine_counter += 1
            machines[machine_counter] += 1
    elif abs(socks_lst[i] - socks_lst[i - 1]) <= colour_diff:
        if machines[machine_counter] < socks_per_machine:
            machines[machine_counter] += 1
        else:
            machine_counter += 1
            machines[machine_counter] += 1
    else:
        machine_counter += 1
        machines[machine_counter] += 1

if 0 in machines:
    machines.remove(0)
print(len(machines))