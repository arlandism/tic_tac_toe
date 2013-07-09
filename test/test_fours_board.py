from fours_board import FourByFourBoard
import unittest

class FourByFourBoardTests(unittest.TestCase):

    def setUp(self):
        self.board = FourByFourBoard()

    def tearDown(self):
        self.board.board_state = {}

    def test_board_over_with_win(self):
        self.board.board_state = {1:"x",2:"x",3:"x",
                             4:"x"}
        self.assertTrue(self.board.over())

    def test_board_over_when_full(self):
        self.board.board_state = {1:"x",2:"o",3:"x",4:"o",
                             5:"x",6:"o",7:"o",8:"x",
                             9:"o",10:"x",11:"o",12:"x",
                             13:"x",14:"o",15:"o",16:"x"}
        self.assertTrue(self.board.over())

    def test_board_not_over_when_empty(self):
        self.assertFalse(self.board.over())



	
        
 
    

    
