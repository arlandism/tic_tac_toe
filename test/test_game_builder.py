import unittest

from game_builder import GameBuilder
from game import Game
from player import HumanPlayer
from prompt_parser import PromptParser

from test_utils import *

class GameBuilderTests(unittest.TestCase):

    def setUp(self):
        self.data = {"Player One": "Fake",
                     "Player Two": "Fake",
                     "board":20}
        self.parser = MockParser(self.data)

    def test_used_parser_passed_in(self):
        game = GameBuilder.game(self.parser)
        self.assertEqual(20,game.board.board_index)

    def test_factory_called(self):
        self.data["Player One"] = "FakePlayerOne"
        factory = MockFactory  
        game = GameBuilder.game(self.parser,factory=factory)
        self.assertEqual("FakePlayerOne",game.player_one)

    def test_display_object_passed_in(self):
        printer = FakePrinter()
        game = GameBuilder.game(self.parser,printer,factory=MockFactory)
        self.assertEqual(printer,game.display_object)

    def test_display_object_reaches_factory(self):
        printer = FakePrinter()





         
