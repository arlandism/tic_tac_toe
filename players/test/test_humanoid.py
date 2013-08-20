import unittest

from players.humanoid import Humanoid
from game.base_board import BaseBoard
from test.test_utils import SimpleMockPrompter, FakePrinter, FakeMinimax

class HumanoidNextMoveTests(unittest.TestCase):

    def setUp(self):
        self.board = BaseBoard(3)
        self.prompter = SimpleMockPrompter

    def tearDown(self):
        self.board.board_state = {}

    def test_first_move_is_human(self):
        mock = self.prompter([1])      
        player = Humanoid("x",mock)
        self.assertEqual(1,player.next_move(self.board))
       
    def test_second_move_is_human(self):
        mock = self.prompter([1,2])
        player = Humanoid("x",mock)
        self.assertEqual(1,player.next_move(self.board))
        self.assertEqual(2,player.next_move(self.board))

    def test_calls_minimax_after_third_move(self):
        player = Humanoid("x",minimax=FakeMinimax(["next move"]))
        player.times_next_move_called = 3
        self.assertEqual("next move", player.next_move(self.board))

    def test_default_minimax_is_impossible_level(self):
        player = Humanoid("x")
        player.times_next_move_called = 3
        self.board.board_state = {1:"x", 4:"o", 5:"o", 7:"x"}
        self.assertEqual(6,player.next_move(self.board))
                         
    def test_for_prompts(self):
        mock = self.prompter([1])
        humanoid = Humanoid("x",mock)
        humanoid.next_move(BaseBoard(3))
        prompts = [humanoid.turn_prompt(),"Available moves are ",humanoid.move_prompt(),"Please select a move: "]
        for prompt in prompts:
            self.assertTrue(prompt in mock.history_string())
