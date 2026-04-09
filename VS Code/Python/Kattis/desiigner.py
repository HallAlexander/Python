s = input()

b_count = s.count('b')
r_count = s.count('r')
vowel_count = sum(c in 'aeiouy' for c in s)

if b_count == 1 and r_count >= 2 and vowel_count == 1:
    if s[0] == 'b' and s[-1] in 'aeiouy':
        print('Jebb')
    else:
        print('Neibb')
else:
    print('Neibb')