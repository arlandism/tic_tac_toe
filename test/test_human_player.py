import unittest

from test_utils import FakePrinter,MockUserInput
from base_board import BaseBoard

from player import *

class PlayerInitTests(unittest.TestCase):

    def test_if_init_function_set_opponent_token(self):
        player = HumanPlayer('o')
        self.assertEqual('x',player.opponent_token)

        player_two = HumanPlayer('x')
        self.assertEqual('o',player_two.opponent_token)

    def test_player_prompts(self):
        mock = MockUserInput([1])
        fake_printer = FakePrinter()
        player = HumanPlayer("x",mock,fake_printer)
        player.next_move(BaseBoard(3))
        available_moves = "Available moves are " + str(BaseBoard(3).available_moves())
        move_prompt = "Please select a move: "
        token_prompt = player.token.capitalize() + "'s turn"
        prompts = [available_moves, move_prompt, token_prompt]
        for prompt in prompts:
            self.assertTrue(prompt in fake_printer.history_string())

