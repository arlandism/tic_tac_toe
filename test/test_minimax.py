import unittest
from board import Board
from minimax import Minimax
from base_board import BaseBoard

class MinimaxNextMoveTests(unittest.TestCase):

    def test_that_it_wins(self):
        board = Board()
	board.board_state = {1:"x",2:"x"}
	self.assertEqual(3,Minimax("x",20).next_move(board))

    def test_that_it_counters(self):
	board = Board()
	board.board_state = {1:"x",2:"x"}
	self.assertEqual(3,Minimax("o",20).next_move(board))

    def test_that_it_anticipates_setup(self):
	board = Board()
	board.board_state = {1:"x"}
	self.assertEqual(5,Minimax("o",20).next_move(board))

    def test_it_is_dumb_with_lower_depths(self):
	board = Board()
	board.board_state = {1:"x"}
	self.assertNotEqual(5,Minimax("o",2).next_move(board))

