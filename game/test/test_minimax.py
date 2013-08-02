import unittest

from game.minimax import Minimax
from game.base_board import BaseBoard

class MinimaxNextMoveTests(unittest.TestCase):

    def setUp(self):
        self.x_minimax = Minimax("x",20)
      	self.o_minimax = Minimax("o",20)
        self.board = BaseBoard(3)

    def tearDown(self):
        self.board.board_state = {} 

    def test_if_minimax_chooses_winning_move_with_threat(self):
        self.board.board_state = {1:"o", 2:"o", 4:"x", 5:"x"} 
        self.assertEqual(3,self.o_minimax.next_move(self.board))

    def test_minimax_move_defense(self):
        computer = self.o_minimax
        self.board.board_state = {1:"o", 5:"x", 9:"x"}
        self.assertTrue(self.o_minimax.next_move(self.board) in (3,7))

    def test_minimax_goes_for_fastest_win(self):
        self.board.board_state = {1:"x", 2:"x"}
        self.assertEqual(3,self.x_minimax.next_move(self.board))

    def test_that_it_counters(self):
        self.board.board_state = {1:"x",2:"x"}
        self.assertEqual(3,self.o_minimax.next_move(self.board))

    def test_that_it_anticipates_setup(self):
        self.board.board_state = {1:"x"}
        self.assertEqual(5,self.o_minimax.next_move(self.board))

    def test_it_is_dumb_with_lower_depths(self):
        self.board.board_state = {1:"x",2:"x"}
        self.assertNotEqual(3,Minimax("o",1).next_move(self.board))

    def test_it_with_four_by_four(self):
        board = BaseBoard(4)
        board.board_state = {1: "x", 2: "x", 3: "x",
                             5: "o", 6: "o", 7: "o", 8: "x",
                             9: "x", 10: "o", 11: "x", 12: "x",
                             13: "o", 14: "x", 15: "o", 16: "x"}
        self.assertEqual(4,self.x_minimax.next_move(board))

    def test_it_with_two_by_two(self):
        board = BaseBoard(2)
        board.board_state = {1:"x",3:"shoe",4:"moo"}
        self.assertEqual(2,self.x_minimax.next_move(board))

