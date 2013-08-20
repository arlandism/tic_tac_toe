import unittest
import mock

from test.test_utils import FakePrinter
from game.base_board import BaseBoard
from game.minimax import Minimax
from players.ai import ImpossibleAI

class AINextMoveTests(unittest.TestCase):

    def test_for_prompts(self):
        board = BaseBoard(3)
        fake_prompter = mock.Mock() 
        fake_prompter.display = mock.MagicMock()
        minimax = mock.Mock()
        minimax.next_move = mock.MagicMock(return_value = 3)
        computer = ImpossibleAI("x",fake_prompter,minimax)
        computer.next_move(board)
        fake_prompter.display.assert_called_with(computer.turn_prompt() + computer.move_prompt() + "3")
	
    def test_next_move_on_empty_board(self):
        board = BaseBoard(3)
        minimax = mock.Mock()
        minimax.next_move = mock.MagicMock(return_value=2)
        ai = ImpossibleAI("x",minimax=minimax)
        self.assertEqual(2,ai.next_move(board))

    def test_next_move_on_board_thats_won(self):
        board = BaseBoard(3)
        board.board_state = {1:"x", 2:"x", 3:"x"}
        ai = ImpossibleAI("x")
        self.assertEqual(None,ai.next_move(board))

    def test_next_move_on_board_won_with_other_token(self):
        board = BaseBoard(3)
        board.board_state = {1:"o", 2:"o", 3:"o"}
        ai = ImpossibleAI("x")
        self.assertEqual(None,ai.next_move(board))

    def test_next_move_on_full_board(self):
        board = BaseBoard(3)
        board.board_state = {1:"x", 2:"o", 3:"x",
                             4:"o", 5:"x", 6:"x",
                             7:"x", 8:"o", 9:"o"}
        ai = ImpossibleAI("x")
        self.assertEqual(None,ai.next_move(board))

class AIIntegrationWithMinimaxTests(unittest.TestCase):

    def test_integration_with_default_minimax(self):
        ai = ImpossibleAI("x") 
        board = BaseBoard(3)
        board.board_state = {1:"x", 2:"x"}
        move = ai.next_move(board)
        self.assertEqual(3,move)

    def test_integration_with_instantiated_minimax(self):
        minimax = Minimax("o",1)
        ai = ImpossibleAI("o",minimax=minimax)
        board = BaseBoard(3)
        self.assertTrue(ai.next_move(board) in range(1,10))

    def test_integration_with_minimax_on_4(self):
        ai = ImpossibleAI("o")
        board = BaseBoard(4)
        move = ai.next_move(board)
        self.assertTrue(move in range(1,17))
