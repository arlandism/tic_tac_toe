import unittest

from test_utils import FakePrinter,MockUserInput
from base_board import BaseBoard

from player import *

class PlayerInitTests(unittest.TestCase):

    def test_if_init_function_sets_token(self):
        player = HumanPlayer('o')
        self.assertEqual(player.token,'o')

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
        history_string = "".join(fake_printer.history)
        NOT_FOUND = -1
        status = history_string.find("Available moves are " + str(BaseBoard(3).available_moves())) 
        self.assertNotEqual(NOT_FOUND,status)
 
        status = history_string.find("Please select a move: ")
        self.assertNotEqual(NOT_FOUND,status)

        status = history_string.find(player.token.capitalize() + "'s turn")
        self.assertNotEqual(NOT_FOUND,status)
