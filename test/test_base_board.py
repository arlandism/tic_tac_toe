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

    def test_winners(self):
        rows = [[1,2,3],
                [4,5,6],
               [7,8,9]]
        columns = [[1,4,7],
                   [2,5,8],
                  [3,6,9]]
        diagonals = [[1,5,9],
                    [3,5,7]]
        winners = rows + columns + diagonals
        self.assertEqual(winners.sort(),BaseBoard(base=3).winners().sort())
        
        winners = [[1,2],[3,4],
                   [1,4],[2,3],
                   [1,3],[2,4]]
        self.assertEqual(winners.sort(),BaseBoard(base=2).winners().sort())

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
