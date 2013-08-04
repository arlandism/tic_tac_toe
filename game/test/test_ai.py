import unittest

from game.base_board import BaseBoard
from test.test_utils import FakePrinter, FakeMinimax

from game.ai import ImpossibleAI

class AiNextMoveTests(unittest.TestCase):

    def test_for_prompts(self):
        fake_printer = FakePrinter()
        computer = ImpossibleAI("x",fake_printer)
        board = BaseBoard(3)
        board.board_state = {1:"x",2:"x"}
        computer.next_move(board)
        self.assertTrue("X turn" in fake_printer.history_string())
        self.assertTrue("x moves to 3" in fake_printer.history_string())
	
    def test_minimax_gets_called(self):
        computer = ImpossibleAI("x",minimax=FakeMinimax(["next move"]))
        self.assertEqual("next move",computer.next_move(BaseBoard(3)))

