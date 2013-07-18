import unittest

from player import HumanPlayer
from ai import ImpossibleAI
from humanoid import Humanoid
from player_factory import PlayerFactory
from base_board import BaseBoard
from test_utils import FakePrinter,SimpleMockPrompter

class PlayerFactoryTests(unittest.TestCase):

    def test_player_with_human(self):
        player = PlayerFactory.player("Human","x")
        self.assertTrue(isinstance(player,HumanPlayer))

    def test_player_with_impossible_ai(self):
        player = PlayerFactory.player("ImpossibleAI","o")
        self.assertTrue(isinstance(player,ImpossibleAI))

    def test_player_with_humanoid(self):
        player = PlayerFactory.player("Humanoid","x")
        self.assertTrue(isinstance(player,Humanoid))

    def test_player_with_easy_ai(self):
        player = PlayerFactory.player("EasyAI","o")
        self.assertTrue(isinstance(player,ImpossibleAI))
        board = BaseBoard(3)
        board.board_state = {1:"x",2:"x"}
        self.assertTrue(player.next_move(board) != 3)

    def test_display_object_passed_in_to_factory(self):
        display_object = SimpleMockPrompter()
        player = PlayerFactory.player("Humanoid","x",display_object)
        self.assertEqual(display_object,player.prompter)
