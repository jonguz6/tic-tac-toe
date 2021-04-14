import io
from unittest import TestCase
from unittest.mock import patch

from tic_tac_toe import BOARD, generate_board, print_board, game_loop


class TestTicTacToe(TestCase):
    board = BOARD.copy()
    generated_board = [f"{board['tL']}|{board['tL']}|{board['tL']}",
                       '-+-+-',
                       f"{board['tL']}|{board['tL']}|{board['tL']}",
                       '-+-+-',
                       f"{board['tL']}|{board['tL']}|{board['tL']}"]
    printed_board = ' | | \n-+-+-\n | | \n-+-+-\n | | \n'

    def setUp(self) -> None:
        pass

    def test_create_empty_board(self):
        self.assertEqual(self.generated_board, list(generate_board(self.board)))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_empty_board(self, mock_out):
        print_board(self.generated_board)
        self.assertEqual(self.printed_board, mock_out.getvalue())

    @patch('sys.stdin', io.StringIO('tR'))
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

    @patch('sys.stdin', io.StringIO('tR\ntL'))
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

    @patch('sys.stdin', io.StringIO('tL\ntM\ntR\nmL\nmM\nmR\nbL\nbM\nbR'))
    def test_game_loop_detects_boar_is_full(self):
        board = self.board.copy()
        full_board = ['X|O|X', '-+-+-', 'O|X|O', '-+-+-', 'X|O|X']
        with patch('sys.stdout', new_callable=io.StringIO) as f:
            try:
                game_loop(board)
            except EOFError:
                pass
            value = f.getvalue()
        self.assertEqual(full_board, value.split('\n')[54:59])
        self.assertEqual("There is no winner!", value.split('\n')[60])
