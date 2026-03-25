def is_complete(paths):
    for p in paths:
        if p == '':
            continue
        parent = p[:-1]
        if parent not in paths:
            return False
    return True

cases = input().split('()')
cases.pop(len(cases)-1)

for i in range(len(cases)):
    cards = cases[i].split(' ')
    cards.pop(len(cards)-1)
    if i > 0: cards.pop(0)
    data = []
    for card in cards:
        card = card.translate(str.maketrans('', '', '()'))
        
        data.append(card.split(','))
    data.sort(key=lambda x: (len(x[1]), x[1]))
    paths = {p for _, p in data}
    if is_complete(paths):
        print(*(value for value, _ in data))
    else:
        print('incomplete')