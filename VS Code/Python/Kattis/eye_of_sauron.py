intext = input()
intext = [*intext]
left_counter = 0
right_counter = 0
index = 0
while(intext[index] != '('):
    left_counter += 1   
    index += 1
index += 2
while(index < len(intext)):
    right_counter += 1
    index += 1
if left_counter - right_counter == 0:
    print('correct')
else:
    print('fix')