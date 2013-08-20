from game import Game
from players.player_factory import PlayerFactory
from base_board import BaseBoard
from io.prompt_parser import PromptParser
from io.prompter import Prompter

class GameBuilder(object):

    @staticmethod
    def game(parser,prompter=None,factory=None):
        if factory is None:  factory = PlayerFactory
        if prompter is None:  prompter=Prompter()
        player_one = factory.player(parser.first_player(),parser.first_token(),prompter)
        player_two = factory.player(parser.second_player(),parser.second_token(),prompter)
        board = BaseBoard(parser.board_size())
        return Game(player_one,player_two,board,prompter)
