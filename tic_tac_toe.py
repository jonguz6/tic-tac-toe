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
    pass


if __name__ == '__main__':
    game_loop(BOARD)
