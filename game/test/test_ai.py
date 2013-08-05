import unittest
import mock

from test.test_utils import FakePrinter

from game.ai import ImpossibleAI

class AiNextMoveTests(unittest.TestCase):

    def test_for_prompts(self):
        fake_printer = FakePrinter()
        minimax = mock.Mock()
        minimax.next_move = mock.MagicMock(return_value = 3)
        computer = ImpossibleAI("x",fake_printer,minimax)
        computer.next_move({})
        self.assertTrue("X turn" in fake_printer.history_string())
        self.assertTrue("x moves to 3" in fake_printer.history_string())
	
    def test_minimax_gets_called(self):
        minimax = mock.Mock()
        minimax.next_move = mock.MagicMock(return_value="next move")
        computer = ImpossibleAI("x",minimax=minimax)
        self.assertEqual("next move",computer.next_move({}))

