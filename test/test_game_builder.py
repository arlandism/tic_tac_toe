import unittest

from game_builder import GameBuilder
from game import Game
from player import HumanPlayer
from prompt_parser import PromptParser
from prompt_store import PromptStore

from test_utils import *

class GameBuilderTests(unittest.TestCase):

    def setUp(self):
        self.data = {"Player One": "Fake",
                     "Player Two": "Fake",
                     "board":20}
        self.fake_data = {PromptStore().player_string(): "Human",
                          PromptStore().first_token():"x",
                          PromptStore().second_player():"Human",
                          PromptStore().board():4}
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
        prompter = SimpleMockPrompter([]) 
        parser = PromptParser(self.fake_data)
        game = GameBuilder.game(parser,prompter)
        self.assertEqual(prompter,game.prompter)

    def test_display_object_reaches_factory_and_players(self):
        printer = FakePrinter()
        parser = PromptParser(self.fake_data)
        game = GameBuilder.game(parser,prompter=printer)
        self.assertEqual(printer,game.player_one.prompter)
