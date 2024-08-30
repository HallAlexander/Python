limits = input().split(' ')
limits = [int(x) for x in limits]
grade = int(input())
grades = ['A', 'B', 'C', 'D', 'E']
printed = False
for i in range(len(limits)):
    if grade >= limits[i] and printed == False:
        print(grades[i])
        printed = True
        
if printed == False:
    print('F')