def normalize(ascii):
    return tuple(ascii)

digits = {
    "0": [
        "xxxxx",
        "x...x",
        "x...x",
        "x...x",
        "x...x",
        "x...x",
        "xxxxx"
    ],
    "1": [
        "....x",
        "....x",
        "....x",
        "....x",
        "....x",
        "....x",
        "....x"
    ],
    "2": [
        "xxxxx",
        "....x",
        "....x",
        "xxxxx",
        "x....",
        "x....",
        "xxxxx"
    ],
    "3": [
        "xxxxx",
        "....x",
        "....x",
        "xxxxx",
        "....x",
        "....x",
        "xxxxx"
    ],
    "4": [
        "x...x",
        "x...x",
        "x...x",
        "xxxxx",
        "....x",
        "....x",
        "....x"
    ],
    "5": [
        "xxxxx",
        "x....",
        "x....",
        "xxxxx",
        "....x",
        "....x",
        "xxxxx"
    ],
    "6": [
        "xxxxx",
        "x....",
        "x....",
        "xxxxx",
        "x...x",
        "x...x",
        "xxxxx"
    ],
    "7": [
        "xxxxx",
        "....x",
        "....x",
        "....x",
        "....x",
        "....x",
        "....x"
    ],
    "8": [
        "xxxxx",
        "x...x",
        "x...x",
        "xxxxx",
        "x...x",
        "x...x",
        "xxxxx"
    ],
    "9": [
        "xxxxx",
        "x...x",
        "x...x",
        "xxxxx",
        "....x",
        "....x",
        "xxxxx"
    ],
    "+": [
        ".....",
        "..x..",
        "..x..",
        "xxxxx",
        "..x..",
        "..x..",
        "....."
    ]
}

ascii_to_char = {
    normalize(digits['0']): '0',
    normalize(digits['1']): '1',
    normalize(digits['2']): '2',
    normalize(digits['3']): '3',
    normalize(digits['4']): '4',
    normalize(digits['5']): '5',
    normalize(digits['6']): '6',
    normalize(digits['7']): '7',
    normalize(digits['8']): '8',
    normalize(digits['9']): '9',
    normalize(digits['+']): '+'
}

rows = [input() for _ in range(7)]
symbols = []
width = len(rows[0])
for col in range(0, width, 6):
    block = [row[col:col+5] for row in rows]
    symbols.append(tuple(block))

    expression = ''
    for sym in symbols:
        expression += ascii_to_char[sym]

left, right = expression.split('+')
result = str(int(left) + int(right))
char_to_ascii = {v: k for k, v in ascii_to_char.items()}

output_rows = [''] * 7
for i, c in enumerate(result):
    pattern = char_to_ascii[c]
    for r in range(7):
        output_rows[r] += pattern[r]
        if i != len(result) - 1:
            output_rows[r] += '.'
print('\n'.join(output_rows))