from game import Game
from player_factory import PlayerFactory
from base_board import BaseBoard
from prompt_parser import PromptParser

class GameBuilder(object):

    @staticmethod
    def game(user_data):
        parser = PromptParser(user_data)
        player_one = PlayerFactory.player(parser.first_player(),parser.first_token())
        player_two = PlayerFactory.player(parser.second_player(),parser.second_token())
        board = BaseBoard(parser.board_size())
        return Game(player_one,player_two,board)
