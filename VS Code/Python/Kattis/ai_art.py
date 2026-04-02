pi = 3.14159265
w, h = map(int, input().split())
c_area = w*h

line = min(w, h)
if (line**2 * pi)/4 >= c_area/2:
    print('circle')
elif line**2 >= c_area/2:
    print('square')
else:
    print('blank')