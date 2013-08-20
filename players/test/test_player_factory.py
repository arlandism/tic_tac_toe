import unittest
import sys

sys.path.append("/Users/arlandislawrence/development/python/tic_tac_toe")
from players.player import HumanPlayer
from players.ai import ImpossibleAI
from players.humanoid import Humanoid
from players.player_factory import PlayerFactory
from game.base_board import BaseBoard
from test.test_utils import FakePrinter,SimpleMockPrompter

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
