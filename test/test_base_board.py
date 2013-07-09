from base_board import BaseBoard
import unittest

class BaseBoardTests(unittest.TestCase):

    def test_make_move(self):
        board = BaseBoard()
        board.make_move(1,"x")
        self.assertEqual({1:"x"},board.state())
