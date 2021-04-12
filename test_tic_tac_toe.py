from unittest import TestCase

from tic_tac_toe import create_empty_board


class TestTicTacToe(TestCase):
    def setUp(self) -> None:
        self.board = [' | | ', '-+-+-', ' | | ', '-+-+-', ' | | ']

    def test_create_empty_board(self):
        self.assertEqual(self.board, create_empty_board())
