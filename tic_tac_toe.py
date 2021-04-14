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


def swap_users(user):
    if user == 'X':
        user = 'O'
    else:
        user = 'X'
    return user


def detect_board_full(board):
    if ' ' not in board.values():
        return True, 'There is no winner!'
    return False, None


def check_if_move_invalid(move, board):
    if board[move] != ' ':
        return True, 'Invalid move! This place is taken, try another one.'
    else:
        return False, None


def game_loop(board):
    game_board = board.copy()
    user = 'X'
    while True:
        generated_board = generate_board(game_board)
        print_board(generated_board)

        board_full = detect_board_full(game_board)
        if board_full[0]:
            print(board_full[1])
            break

        move = input("What is your move? (tL, tM, tR, mL, mM, mR, bL, bM, bR)\n")

        invalid_move = check_if_move_invalid(move, game_board)
        if invalid_move[0]:
            print(invalid_move[1])
            continue

        game_board[move] = user

        user = swap_users(user)


if __name__ == '__main__':
    game_loop(BOARD)
