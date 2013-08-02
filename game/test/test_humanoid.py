import unittest

from game.humanoid import Humanoid
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

    def test_gets_minimax(self):
        mock = self.prompter([1,2,5])
        player = Humanoid("x",self.prompter([1,2,5]),
        minimax=FakeMinimax())
        for i in range(3):
            player.next_move(self.board)
        self.assertEqual("next move", player.next_move(self.board))

    def test_third_move_is_ai(self):
        mock = self.prompter([1,7])
        player = Humanoid("x",mock)
        self.board.board_state = {4:"o", 5:"o"}
        self.assertEqual(1,player.next_move(self.board))

        self.board.board_state = {1:"x", 4:"o", 5:"o"}
        self.assertEqual(7,player.next_move(self.board))

        self.board.board_state = {1:"x", 4:"o", 5:"o", 7:"x"}
        self.assertEqual(6,player.next_move(self.board))
                         
    def test_for_prompts(self):
        mock = self.prompter([1])
        humanoid = Humanoid("x",mock)
        humanoid.next_move(BaseBoard(3))
        prompts = ["X turn","Available moves are ","X moves to 1","Please select a move: "]
        for prompt in prompts:
            self.assertTrue(prompt in mock.history_string())
