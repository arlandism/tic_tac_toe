import unittest

from game_builder import GameBuilder
from game import Game
from player import HumanPlayer

class MockFactory(object):

    @staticmethod
    def player(player_type,token):
        return {player_type:token} 

class MockParser(object):

    def __init__(self,user_data):
        self.user_data = user_data

    def data(self):
        return self.user_data

    def first_player(self):
        return "Player One"

    def first_token(self):
        return "first token"

    def second_player(self):
        return "Player Two"

    def second_token(self):
        return "second token"

    def board_size(self):
        return "board size"

class MockGame(object):

    def __init__(self,player,other_player,board):
        self.player = player
        self.player_t = other_player
        self.gameboard = board

    def player_one(self):
        return self.player

    def player_two(self):
        return self.player_t

    def board(self):
        return self.gameboard.size

class MockBoard(object):

    def __init__(self,number):
       self.number = number

    def size(self):
        return self.number

class GameBuilderTests(unittest.TestCase):
    pass
