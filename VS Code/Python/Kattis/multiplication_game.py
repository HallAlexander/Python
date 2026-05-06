import sys

for line in sys.stdin:
    p = int(line.strip())
    x = 1
    while x < p:
        x *= 18
    prev = x/18
    if p <= 9*prev:
        print('Stan wins.')
    else:  
        print('Ollie Wins.')