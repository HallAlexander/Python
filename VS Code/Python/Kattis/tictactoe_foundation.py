board = [['.' for _ in range(3)] for _ in range(3)]

pieces = {
    'x': 4,
    'X': 2,
    'o': 4,
    'O': 2
}
large_pos = {'X': [], 'O': []}

def read():
    first = input().strip()
    if first in {'Sigur!', 'Tap!'}:
        exit()

    second = input().strip()
    third = input().strip()
    return [list(first), list(second), list(third)]

def print_board(board):
    for row in board:
        print(''.join(row), flush=True)

def check_winner(board):
    lines = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a,b,c in lines:
        first = board[a//3][a%3]
        if first != '.' and first.lower() == board[b//3][b%3].lower() == board[c//3][c%3].lower():
            return first.lower()
    return None

def compute(board):
    global pieces, large_pos
    
    return board

board = compute(board)
print_board(board)

while True:
    board = read()
    board = compute(board)
    print_board(board)
