import unittest

from board import Board
from test_utils import FakePrinter, FakeMinimax

from ai import *

class AiNextMoveTests(unittest.TestCase):

    def test_for_prompts(self):
        fake_printer = FakePrinter()
	computer = ImpossibleAI("x",fake_printer)
	board = Board()
	board.board_state = {1:"x",2:"x"}
	computer.next_move(board)
	history_string = "".join(fake_printer.history)
	NOT_FOUND = -1
	status = history_string.find("X's turn")
	self.assertNotEqual(NOT_FOUND,status)
	
	status = history_string.find("x moves to 3")
	self.assertNotEqual(NOT_FOUND,status)

    def test_minimax_gets_called(self):
        computer = ImpossibleAI("x")
        fake_minimax = FakeMinimax() 
	self.assertEqual("next move",computer.next_move(Board(),fake_minimax))

