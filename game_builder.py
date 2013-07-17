from game import Game
from player_factory import PlayerFactory
from base_board import BaseBoard
from prompt_parser import PromptParser
from prompter import Prompter

class GameBuilder(object):

    @staticmethod
    def game(parser,display_object=None,factory=None):
        if factory is None:  factory = PlayerFactory
        if display_object is None:  display_object=Prompter()
        player_one = factory.player(parser.first_player(),parser.first_token())
        player_two = factory.player(parser.second_player(),parser.second_token())
        board = BaseBoard(parser.board_size())
        return Game(player_one,player_two,board,display_object)
