def create_empty_board():
    board = {
        'tL': ' ', 'tM': ' ', 'tR': ' ',
        'mL': ' ', 'mM': ' ', 'mR': ' ',
        'bL': ' ', 'bM': ' ', 'bR': ' ',
    }
    return [
        f"{board['tL']}|{board['tM']}|{board['tR']}",
        '-+-+-',
        f"{board['mL']}|{board['mM']}|{board['mR']}",
        '-+-+-',
        f"{board['bL']}|{board['bM']}|{board['bR']}"
    ]


def print_board(board):
    pass


if __name__ == '__main__':
    game_board = create_empty_board()
    print_board(game_board)
