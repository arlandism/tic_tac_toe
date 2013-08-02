import unittest

from game.win_generator import WinGenerator

class WinGeneratorTests(unittest.TestCase):

    def test_rows(self):
        self.assertEqual([[1,2,3],[4,5,6],[7,8,9]],WinGenerator(index=3).rows())

    def test_columns(self):
        self.assertEqual([[1,3],[2,4]],WinGenerator(index=2).columns())
        self.assertEqual([[1,4,7],[2,5,8],[3,6,9]],WinGenerator(index=3).columns())

    def test_diagonals(self):
        self.assertEqual([[1,5,9],[3,5,7]],WinGenerator(index=3).diagonals())
        self.assertEqual([[1,4],[2,3]],WinGenerator(index=2).diagonals())

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
        self.assertEqual(winners.sort(),WinGenerator(index=3).winners().sort())
        
        winners = [[1,2],[3,4],
                   [1,4],[2,3],
                   [1,3],[2,4]]
        self.assertEqual(winners.sort(),WinGenerator(index=2).winners().sort())


