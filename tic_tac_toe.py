def create_empty_board():
    board = {
        'tL': ' ', 'tM': ' ', 'tR': ' ',
        'mL': ' ', 'mM': ' ', 'mR': ' ',
        'bL': ' ', 'bM': ' ', 'bR': ' ',
    }
    yield f"{board['tL']}|{board['tM']}|{board['tR']}"
    yield '-+-+-'
    yield f"{board['mL']}|{board['mM']}|{board['mR']}"
    yield '-+-+-'
    yield f"{board['bL']}|{board['bM']}|{board['bR']}"


def print_board(board):
    for line in board:
        print(line)


if __name__ == '__main__':
    game_board = create_empty_board()
    print_board(game_board)
