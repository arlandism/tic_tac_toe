from player import HumanPlayer
from game import Game
from no_prompt_interface import NoPromptInterface	

class HumanVsHumanScenario(object):

    def setup(self):
	player_one = HumanPlayer("x")
	player_two = HumanPlayer("o")
	return Game(player_one,player_two)

    @staticmethod
    def flags():
        return {"difficulty_flag":False,
		"token_flag":False,
		"order_flag":False}
    @staticmethod
    def prompts():
	return NoPromptInterface.prompts()
