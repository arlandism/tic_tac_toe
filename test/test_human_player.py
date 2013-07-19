import unittest

from test_utils import FakePrinter,MockUserInput,SimpleMockPrompter
from base_board import BaseBoard

from player import *

class PlayerInitTests(unittest.TestCase):

    def test_prompter_passed_in(self):
        prompter = SimpleMockPrompter
        player = HumanPlayer("x",prompter=prompter)
        self.assertEqual(prompter,player.prompter)

    def test_player_prompts(self):
        mock = SimpleMockPrompter([1])
        player = HumanPlayer("x",mock)
        player.next_move(BaseBoard(3))
        available_moves = "\nAvailable moves are " + str(BaseBoard(3).available_moves())
        move_prompt = "\nPlease select a move: "
        token_prompt = player.token.capitalize() + " turn"
        prompts = [available_moves, move_prompt, token_prompt]
        for prompt in prompts:
            self.assertTrue(prompt in mock.history_string())
