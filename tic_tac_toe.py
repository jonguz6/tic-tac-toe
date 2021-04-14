BOARD = {
    'tL': ' ', 'tM': ' ', 'tR': ' ',
    'mL': ' ', 'mM': ' ', 'mR': ' ',
    'bL': ' ', 'bM': ' ', 'bR': ' ',
}
NUMPAD = {
    7: 'tL', 8: 'tM', 9: 'tR',
    4: 'mL', 5: 'mM', 6: 'mR',
    1: 'bL', 2: 'bM', 3: 'bR'
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
    try:
        board[move]
    except KeyError:
        return True, 'Invalid move! Please use one of the values hinted below.'
    else:
        if board[move] != ' ':
            return True, 'Invalid move! This place is taken, try another one.'
        else:
            return False, None


def check_if_three_values_are_the_same(x, y, z):
    if x == y == z != ' ':
        return True
    return False


def check_for_winner(board):
    combinations = (
        ('tL', 'tM', 'tR'),
        ('tL', 'mM', 'bR'),
        ('tL', 'mL', 'bL'),
        ('tM', 'mM', 'bM'),
        ('mL', 'mM', 'mR'),
        ('tR', 'mR', 'bR'),
        ('bL', 'bM', 'bR'),
        ('bL', 'mM', 'tR')
    )
    for combination in combinations:
        x = combination[0]
        y = combination[1]
        z = combination[2]

        if check_if_three_values_are_the_same(board[x], board[y], board[z]):
            return True, board[x]
        continue
    return False, None


def check_for_numpad():
    numpad = input("Do you want to play with a numpad/numerical keys? (Y/n)")
    if numpad.lower() == 'y' or numpad == '':
        return True
    return False


def translate_num_to_dict_key(number, trans_table=None):
    number = int(number)
    if trans_table is None:
        trans_table = NUMPAD
    try:
        result = trans_table[number]
    except KeyError:
        result = None
    return result


def game_loop(board):
    game_board = board.copy()
    user = 'X'
    numpad = check_for_numpad()

    while True:
        generated_board = generate_board(game_board)
        print_board(generated_board)

        check, winner = check_for_winner(game_board)
        if winner:
            print(f'Congratulations! The winner is {winner}!')
            break

        board_full = detect_board_full(game_board)
        if board_full[0]:
            print(board_full[1])
            break

        move = input("What is your move? (tL, tM, tR, mL, mM, mR, bL, bM, bR)\n")
        if numpad:
            move = translate_num_to_dict_key(move)
        invalid_move = check_if_move_invalid(move, game_board)
        if invalid_move[0]:
            print(invalid_move[1])
            continue

        game_board[move] = user

        user = swap_users(user)


if __name__ == '__main__':
    game_loop(BOARD)
