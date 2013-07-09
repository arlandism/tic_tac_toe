from base_board import BaseBoard
import unittest

class BaseBoardTests(unittest.TestCase):

    def test_make_move(self):
        board = BaseBoard()
        board.make_move(1,"x")
        self.assertEqual({1:"x"},board.state())

    def test_winner(self):
        board = BaseBoard(base=3)
        board.board_state = {1:"me",2:"me",3:"me"}
        self.assertEqual("me",board.winner())

        new_board = BaseBoard(base=2)
        new_board.board_state = {1:"you",4:"you"}
        self.assertEqual("you",new_board.winner())

    def test_full(self):
        board = BaseBoard(base=3)
        board.board_state = {1:"o",2:"o",3:"x",
                             4:"x",5:"x",6:"o",
                             7:"o",8:"o",9:"x"}
        self.assertTrue(board.is_full())
        self.assertFalse(BaseBoard(base=2).is_full())

    def test_available_moves(self):
        self.assertEqual(range(1,17),BaseBoard(base=4).available_moves())
        self.assertEqual(range(1,5),BaseBoard(base=2).available_moves())
        board = BaseBoard(base=2)
        board.board_state = {4:"x"}
        self.assertEqual(range(1,4),board.available_moves())

    def test_erase_move(self):
        board = BaseBoard(base=2)
        board.make_move(3,"x")
        board.erase_move(3)
        self.assertEqual({},board.state())

    def test_over(self):
        self.assertFalse(BaseBoard(base=3).over())
        board = BaseBoard(base=3)
        board.board_state = {1:"x",2:"x",3:"x"}
      #  self.assertTrue(board.over())
       
