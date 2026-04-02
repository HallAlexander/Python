def write(string, rule, replacement, step, max_len=255, max_steps=5000):
    
    while step <= max_steps and len(string) <= max_len:
        changed = False
        for i in range(len(rule)):
            new_string = string.replace(rule[i], replacement[i], 1)

            if new_string != string:
                string = new_string
                step += 1
                changed = True
                break
        if not changed:
            break
    if step > max_steps:
        print('Time Limit Exceeded')
        quit()
    elif len(string) > max_len:
        print('Memory Limit Exceeded')
        quit()
    return string, step

string = input()
no_of_rules = int(input())
rule, replacement = [], []
for _ in range(no_of_rules):
    tmp, tmp2 = input().split('=')
    rule.append(tmp)
    replacement.append(tmp2)
count = 0
result, steps = write(string, rule, replacement, count)
print(result)
