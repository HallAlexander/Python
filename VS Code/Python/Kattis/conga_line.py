couples, instr_size = map(int, input().split())

name_to_id = {}
id_to_name = []
partner_id = []
line_ids = []

for _ in range(couples):
    first, second = input().split()
    for name in (first, second):
        if name not in name_to_id:
            idx = len(id_to_name)
            name_to_id[name] = idx
            id_to_name.append(name)
            partner_id.append(-1)
    idx1 = name_to_id[first]
    idx2 = name_to_id[second]
    partner_id[idx1] = idx2
    partner_id[idx2] = idx1
    line_ids.append(idx1)
    line_ids.append(idx2)

instructions = input()

N = len(line_ids)
next_idx = [-1]*N
prev_idx = [-1]*N

for i in range(N):
    if i > 0:
        prev_idx[line_ids[i]] = line_ids[i-1]
    if i < N-1:
        next_idx[line_ids[i]] = line_ids[i+1]

head = line_ids[0]
tail = line_ids[-1]
mic = head

def f(mic):
    return prev_idx[mic] if prev_idx[mic] != -1 else tail

def b(mic):
    return next_idx[mic] if next_idx[mic] != -1 else head

def r(mic):
    global head, tail
    if next_idx[mic] == -1:
        return head
    nxt = next_idx[mic]

    p = prev_idx[mic]
    n = next_idx[mic]
    if p != -1:
        next_idx[p] = n
    if n != -1:
        prev_idx[n] = p
    if mic == head:
        head = n

    prev_idx[mic] = tail
    next_idx[mic] = -1
    next_idx[tail] = mic
    tail = mic

    return nxt

def c(mic):
    global head, tail
    partner = partner_id[mic]
    nxt = next_idx[mic] if next_idx[mic] != -1 else head

    p = prev_idx[mic]
    n = next_idx[mic]
    if p != -1:
        next_idx[p] = n
    if n != -1:
        prev_idx[n] = p
    if mic == head:
        head = n
    if mic == tail:
        tail = p

    after = next_idx[partner]
    next_idx[partner] = mic
    prev_idx[mic] = partner
    next_idx[mic] = after
    if after != -1:
        prev_idx[after] = mic
    else:
        tail = mic

    return nxt

def p(mic):
    print(id_to_name[partner_id[mic]])

for instr in instructions:
    match instr:
        case 'F':
            mic = f(mic)
        case 'B':
            mic = b(mic)
        case 'R':
            mic = r(mic)
        case 'C':
            mic = c(mic)
        case 'P':
            p(mic)

print()
curr = head
while curr != -1:
    print(id_to_name[curr])
    curr = next_idx[curr]


"""def f (mic):
    return prev[mic] if prev[mic] is not None else mic

def b (mic):
    return next[mic] if next[mic] is not None else mic

def r (mic):
    if next[mic] is None:
        return head
    nxt = next[mic]
    p = prev[mic]
    n = next[mic]

    if p: next[p] = n
    if n: prev[n] = p

    prev[mic] = tail
    next[mic] = None
    next[tail] = mic
    global tail
    tail = mic
    return nxt

def c (mic):
    partner = partner_list[mic]

    nxt = next[mic] if next[mic] is not None else head
    p = prev[mic]
    n = next[mic]
    if p: next[p] = n
    if n: prev[n] = p

    after = next[partner]
    next[partner] = mic
    prev[mic] = partner
    next[mic] = after
    if after:
        prev[after] = mic
    global tail
    if tail == partner:
        tail = mic

    return nxt
  
    
def p (mic):
    print(partner_list[mic])

couples, instr_size = map(int, input().split())

head = None
tail = None
next = {}
prev = {}

line = []
partner_list = {}


for _ in range(couples):
    first, second = input().split()
    line.append(first)
    line.append(second)
    partner_list[first] = second
    partner_list[second] = first

for i, name in enumerate(line):
    if i == 0:
        head = name
        prev[name] = None
    else:
        prev[name] = line[i-1]
        next[line[i-1]] = name
    if i == len(line) -1 :
        tail = name
        next[name] = None
mic = head
instructions = input()
for instruction in instructions:
    match instruction:
        case 'F':
            mic = f(mic)
        case 'B':
            mic = b(mic)
        case 'R':
            mic = r(mic)
        case 'C':
            mic = c(mic)
        case 'P':
            p(mic)
print()
curr = head
while curr is not None:
    print(curr)
    curr = next[curr]
"""