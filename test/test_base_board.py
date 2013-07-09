from base_board import BaseBoard
import unittest

class BaseBoardTests(unittest.TestCase):

    def test_make_move(self):
        board = BaseBoard()
        board.make_move(1,"x")
        self.assertEqual({1:"x"},board.state())

    def test_rows(self):
        self.assertEqual([[1,2,3],[4,5,6],[7,8,9]],BaseBoard(base=3).rows())
