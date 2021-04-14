BOARD = {
    'tL': ' ', 'tM': ' ', 'tR': ' ',
    'mL': ' ', 'mM': ' ', 'mR': ' ',
    'bL': ' ', 'bM': ' ', 'bR': ' ',
}


def generate_board(board):
    yield f"{board['tL']}|{board['tM']}|{board['tR']}"
    yield '-+-+-'
    yield f"{board['mL']}|{board['mM']}|{board['mR']}"
    yield '-+-+-'
    yield f"{board['bL']}|{board['bM']}|{board['bR']}"


def print_board(board):
    for line in board:
        print(line)


def game_loop(board):
    game_board = board.copy()
    while True:
        generated_board = generate_board(game_board)
        print_board(generated_board)

        move = input("What is your move? (tL, tM, tR, mL, mM, mR, bL, bM, bR)\n")
        game_board[move] = 'X'


if __name__ == '__main__':
    game_loop(BOARD)
