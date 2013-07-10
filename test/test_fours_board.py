from fours_board import FourByFourBoard
import unittest

class FourByFourBoardTests(unittest.TestCase):

    def setUp(self):
        self.board = FourByFourBoard()

    def tearDown(self):
        self.board.board_state = {}

    def test_board_string_with_token(self):
        self.board.board_state = {1:"fake_token"}
	board_string = self.board.__str__()
	NOT_FOUND = -1
	self.assertNotEqual(NOT_FOUND,board_string.find("fake_token"))
