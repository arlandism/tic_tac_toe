import unittest
import mock

from game.game_builder import GameBuilder
from game.game import Game

class GameBuilderTests(unittest.TestCase):
        
    def build_fake_parser(self):
        parser = mock.Mock()
        parser.first_player = mock.MagicMock(return_value="Human")
        parser.first_token = mock.MagicMock(return_value="x")
        parser.second_player = mock.MagicMock(return_value="Human")
        parser.second_token = mock.MagicMock(return_value="o")
        parser.board_size = mock.MagicMock(return_value=4)
        return parser

    def test_used_parser_passed_in(self):
        parser = mock.Mock()
        parser.board_size = mock.MagicMock(return_value=20)
        game = GameBuilder.game(parser)
        self.assertEqual(20,game.board.board_index)

    def test_factory_called(self):
        factory = mock.Mock()
        parser = self.build_fake_parser()
        game = GameBuilder.game(parser,factory=factory)
        self.assertEqual(2, factory.player.call_count)

    def test_display_object_passed_in_to_game(self):
        prompter = mock.Mock() 
        parser = self.build_fake_parser()
        game = GameBuilder.game(parser,prompter)
        self.assertEqual(prompter,game.prompter)

    def test_display_object_reaches_factory_and_players(self):
        printer = mock.Mock()
        parser = self.build_fake_parser()
        game = GameBuilder.game(parser,prompter=printer)
        self.assertEqual(printer,game.player_one.prompter)
