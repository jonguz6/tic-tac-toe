import io
from unittest import TestCase
from unittest.mock import patch

from tic_tac_toe import BOARD, generate_board, print_board, game_loop, swap_users, check_if_move_invalid, \
    detect_board_full, check_if_three_values_are_the_same, check_for_winner, check_for_numpad, \
    translate_num_to_dict_key, NUMPAD


class TestTicTacToe(TestCase):

    def setUp(self) -> None:
        self.board = BOARD.copy()
        self.generated_board = [f"{self.board['tL']}|{self.board['tL']}|{self.board['tL']}",
                                '-+-+-',
                                f"{self.board['tL']}|{self.board['tL']}|{self.board['tL']}",
                                '-+-+-',
                                f"{self.board['tL']}|{self.board['tL']}|{self.board['tL']}"]
        self.printed_board = ' | | \n-+-+-\n | | \n-+-+-\n | | \n'

    def test_create_empty_board(self):
        self.assertEqual(self.generated_board, list(generate_board(self.board)))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_empty_board(self, mock_out):
        print_board(self.generated_board)
        self.assertEqual(self.printed_board, mock_out.getvalue())

    @patch('sys.stdin', io.StringIO('n\ntR'))
    def test_game_loop_takes_one_input(self):
        board = self.board.copy()
        one_input_board = [' | |X', '-+-+-', ' | | ', '-+-+-', ' | | ']
        with patch('sys.stdout', new_callable=io.StringIO) as f:
            try:
                game_loop(board)
            except EOFError:
                pass
            value = f.getvalue()
        self.assertEqual(one_input_board, value.split('\n')[6:11])

    @patch('sys.stdin', io.StringIO('n\ntR\ntL'))
    def test_game_loop_takes_two_inputs(self):
        board = self.board.copy()
        two_input_board = ['O| |X', '-+-+-', ' | | ', '-+-+-', ' | | ']
        with patch('sys.stdout', new_callable=io.StringIO) as f:
            try:
                game_loop(board)
            except EOFError:
                pass
            value = f.getvalue()
        self.assertEqual(two_input_board, value.split('\n')[12:17])

    @patch('sys.stdin', io.StringIO('n\ntL\ntM\ntR\nmM\nmL\nmR\nbM\nbL\nbR'))
    def test_game_loop_detects_boar_is_full(self):
        board = self.board.copy()
        full_board = ['X|O|X', '-+-+-', 'X|O|O', '-+-+-', 'O|X|X']
        with patch('sys.stdout', new_callable=io.StringIO) as f:
            try:
                game_loop(board)
            except EOFError:
                pass
            value = f.getvalue()
        self.assertEqual(full_board, value.split('\n')[54:59])
        self.assertEqual("There is no winner!", value.split('\n')[-2])

    @patch('sys.stdin', io.StringIO('n\ntL\ntL'))
    def test_game_loop_detects_move_on_occupied_cell(self):
        board = self.board.copy()
        with patch('sys.stdout', new_callable=io.StringIO) as f:
            try:
                game_loop(board)
            except EOFError:
                pass
            value = f.getvalue()
        self.assertEqual('Invalid move! This place is taken, try another one.', value.split('\n')[-8])

    @patch('sys.stdin', io.StringIO('n\ntB'))
    def test_game_loop_detects_move_invalid(self):
        board = self.board.copy()
        with patch('sys.stdout', new_callable=io.StringIO) as f:
            try:
                game_loop(board)
            except EOFError:
                pass
            value = f.getvalue()
        self.assertEqual('Invalid move! Please use one of the values hinted below.', value.split('\n')[-8])

    @patch('sys.stdin', io.StringIO('n\ntL\nbL\ntM\nbM\ntR'))
    def test_game_loop_detects_winner(self):
        board = self.board.copy()
        with patch('sys.stdout', new_callable=io.StringIO) as f:
            try:
                game_loop(board)
            except EOFError:
                pass
            value = f.getvalue()
        self.assertEqual('Congratulations! The winner is X!', value.split('\n')[-2])

    @patch('sys.stdin', io.StringIO('n\nmM\ntR\nmR\nmL\nbM\ntM\ntL\nbL\nbR'))
    def test_game_loop_detects_winner_second_scenario(self):
        board = self.board.copy()
        with patch('sys.stdout', new_callable=io.StringIO) as f:
            try:
                game_loop(board)
            except EOFError:
                pass
            value = f.getvalue()
        self.assertEqual('Congratulations! The winner is X!', value.split('\n')[-2])

    @patch('sys.stdin', io.StringIO('n\nmL\nmM\nbM\nbL\ntR\nbR\ntM\ntL'))
    def test_game_loop_detects_winner_third_scenario(self):
        board = self.board.copy()
        with patch('sys.stdout', new_callable=io.StringIO) as f:
            try:
                game_loop(board)
            except EOFError:
                pass
            value = f.getvalue()
        self.assertEqual('Congratulations! The winner is O!', value.split('\n')[-2])

    @patch('sys.stdin', io.StringIO('y\n9'))
    def test_game_loop_takes_input_with_numpad(self):
        board = self.board.copy()
        one_input_board = [' | |X', '-+-+-', ' | | ', '-+-+-', ' | | ']
        with patch('sys.stdout', new_callable=io.StringIO) as f:
            try:
                game_loop(board)
            except EOFError:
                pass
            value = f.getvalue()
        self.assertEqual(one_input_board, value.split('\n')[6:11])

    @patch('sys.stdin', io.StringIO('y\n9\n7'))
    def test_game_loop_takes_two_inputs_with_numpad(self):
        board = self.board.copy()
        two_input_board = ['O| |X', '-+-+-', ' | | ', '-+-+-', ' | | ']
        with patch('sys.stdout', new_callable=io.StringIO) as f:
            try:
                game_loop(board)
            except EOFError:
                pass
            value = f.getvalue()
        self.assertEqual(two_input_board, value.split('\n')[12:17])


class FunctionsTest(TestCase):

    def setUp(self) -> None:
        self.board = BOARD.copy()
        self.NUMPAD = NUMPAD.copy()

    def test_swap_users_function_swaps_correctly(self):
        user = 'X'
        user = swap_users(user)
        self.assertEqual(user, 'O')
        user = swap_users(user)
        self.assertEqual(user, 'X')

    def test_detect_board_full_passes_board_empty(self):
        check, message = detect_board_full(self.board)
        self.assertEqual(check, False)
        self.assertEqual(message, None)

    def test_detect_board_full_passes_board_not_empty_bot_not_full(self):
        board = self.board.copy()
        for key in ('tL', 'mM', 'mR', 'bL'):
            board[key] = 'X'
        check, message = detect_board_full(board)
        self.assertEqual(check, False)
        self.assertEqual(message, None)

    def test_detect_board_full_detects_full_board(self):
        board = self.board.copy()
        for key in board:
            board[key] = 'X'
        check, message = detect_board_full(board)
        self.assertEqual(check, True)
        self.assertEqual(message, "There is no winner!")

    def test_invalid_move_recognizes_invalid_move(self):
        move = 'tB'
        check, message = check_if_move_invalid(move, self.board)
        self.assertEqual(check, True)
        self.assertEqual(message, 'Invalid move! Please use one of the values hinted below.')

    def test_invalid_move_passes_valid_move(self):
        move = 'tR'
        check, message = check_if_move_invalid(move, self.board)
        self.assertEqual(check, False)
        self.assertEqual(message, None)

    def test_invalid_move_recognizes_occupied_move(self):
        board = self.board.copy()
        board['tL'] = 'X'
        move = 'tL'
        check, message = check_if_move_invalid(move, board)
        self.assertEqual(check, True)
        self.assertEqual(message, 'Invalid move! This place is taken, try another one.')
        
    def test_check_if_three_values_are_the_same_with_valid(self):
        x, y, z = 1, 1, 1
        self.assertTrue(check_if_three_values_are_the_same(x, y, z))

    def test_check_if_three_values_are_the_same_with_one_invalid(self):
        x, y, z = 2, 1, 1
        self.assertFalse(check_if_three_values_are_the_same(x, y, z))

    def test_check_if_three_values_are_the_same_with_two_invalid(self):
        x, y, z = 2, 3, 1
        self.assertFalse(check_if_three_values_are_the_same(x, y, z))

    def test_check_if_three_values_are_the_same_with_one_empty(self):
        x, y, z = 2, 3, ' '
        self.assertFalse(check_if_three_values_are_the_same(x, y, z))

    def test_check_if_three_values_are_the_same_with_two_empty(self):
        x, y, z = 2, ' ', ' '
        self.assertFalse(check_if_three_values_are_the_same(x, y, z))

    def test_check_if_three_values_are_the_same_with_all_empty(self):
        x, y, z = ' ', ' ', ' '
        self.assertFalse(check_if_three_values_are_the_same(x, y, z))

    def test_check_for_winner_row_is_X(self):
        board = self.board.copy()
        board['tL'] = "X"
        board['tM'] = "X"
        board['tR'] = "X"
        check, winner = check_for_winner(board)
        self.assertTrue(check)
        self.assertEqual(winner, 'X')

    def test_check_for_winner_column_is_O(self):
        board = self.board.copy()
        board['tM'] = 'O'
        board['mM'] = 'O'
        board['bM'] = 'O'
        check, winner = check_for_winner(board)
        self.assertTrue(check)
        self.assertEqual(winner, 'O')

    def test_check_for_winner_diagonal_is_O(self):
        board = self.board.copy()
        board['bL'] = 'O'
        board['mM'] = 'O'
        board['tR'] = 'O'
        check, winner = check_for_winner(board)
        self.assertTrue(check)
        self.assertEqual(winner, 'O')

    def test_check_for_numpad_no_input(self):
        result = check_for_numpad('')
        self.assertTrue(result)

    def test_check_for_numpad_lowercase_y(self):
        result = check_for_numpad('y')
        self.assertTrue(result)

    def test_check_for_numpad_uppercase_Y(self):
        result = check_for_numpad('Y')
        self.assertTrue(result)

    def test_check_for_numpad_lowercase_n(self):
        result = check_for_numpad('n')
        self.assertFalse(result)

    def test_check_for_numpad_random_input(self):
        result = check_for_numpad('gdasfgertsgh')
        self.assertFalse(result)

    def test_translate_num_to_dict_key_with_good_input(self):
        result = translate_num_to_dict_key(9, self.NUMPAD)
        self.assertEqual(result, 'tR')

    def test_translate_num_to_dict_key_with_bad_input(self):
        result = translate_num_to_dict_key('y', self.NUMPAD)
        self.assertEqual(result, None)

