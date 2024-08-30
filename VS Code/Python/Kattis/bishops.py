import sys
for line in sys.stdin:
    in_number = int(line.strip())
    if in_number == 1:
        out_number = 1
    else:
        out_number = 2*in_number - 2
    print(out_number)
    