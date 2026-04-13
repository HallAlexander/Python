s = input()
out = [s[0]]
for c in s[1:]:
    if c != out[-1]:
        out.append(c)
print(''.join(out))