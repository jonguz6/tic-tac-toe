import io
from unittest import TestCase
from unittest.mock import patch

from tic_tac_toe import create_empty_board, print_board


class TestTicTacToe(TestCase):
    def setUp(self) -> None:
        self.board = [' | | ', '-+-+-', ' | | ', '-+-+-', ' | | ']

    def test_create_empty_board(self):
        self.assertEqual(self.board, list(create_empty_board()))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_empty_board(self, mock_out):
        print_board(self.board)
        printed_board = ' | | \n-+-+-\n | | \n-+-+-\n | | \n'
        self.assertEqual(printed_board, mock_out.getvalue())

