import io
from unittest import TestCase
from unittest.mock import patch

from tic_tac_toe import BOARD, create_empty_board, print_board, game_loop


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
        self.assertEqual(self.generated_board, list(create_empty_board(self.board)))

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
