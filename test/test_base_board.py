from base_board import BaseBoard
import unittest

class BaseBoardTests(unittest.TestCase):

    def test_make_move(self):
        board = BaseBoard()
        board.make_move(1,"x")
        self.assertEqual({1:"x"},board.state())

    def test_rows(self):
        self.assertEqual([[1,2,3],[4,5,6],[7,8,9]],BaseBoard(base=3).rows())

    def test_columns(self):
        self.assertEqual([[1,3],[2,4]],BaseBoard(base=2).columns())
        self.assertEqual([[1,4,7],[2,5,8],[3,6,9]],BaseBoard(base=3).columns())

    def test_diagonals(self):
        self.assertEqual([[1,5,9],[3,5,7]],BaseBoard(base=3).diagonals())
        self.assertEqual([[1,4],[2,3]],BaseBoard(base=2).diagonals())
