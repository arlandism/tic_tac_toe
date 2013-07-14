from player import HumanPlayer
from game import Game
from no_prompt_interface import NoPromptInterface	
from base_board import BaseBoard

class HumanVsHumanScenario(object):

    def __init__(self,user_data):
        self.board_size = user_data.get("What size board would you like (3,4): ") 

    def setup(self):
        player_one = HumanPlayer("x")
        player_two = HumanPlayer("o")
        board = BaseBoard(self.board_size)
        return Game(player_one,player_two,board)

    @staticmethod
    def prompts(more_prompts):
        return NoPromptInterface.prompts(more_prompts)
