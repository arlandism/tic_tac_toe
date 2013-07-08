from game import Game
from humanoid import Humanoid
from easy_ai import EasyAI
from ai import ImpossibleAI
from human_prompt_interface import HumanPromptInterface

class HumanoidVsAiScenario(object):

    def __init__(self,user_data):
	order = user_data.get("Would you like to move first or second (1,2): ")
	player_one_token = user_data.get("Would you like to play as x or o: ")
	player_two_token = {"x":"o","o":"x"}[player_one_token]
	self.humanoid_first = {1:True,2:False}[order]
	difficulty = user_data.get("Would you like to play against an easy or impossible ai: ")
	self.token_one = player_one_token
        self.token_two = player_two_token
	self.difficulty = difficulty
	self.ai_hash = {"easy":EasyAI,"impossible":ImpossibleAI}

    def setup(self):
	ai_object = self.ai_hash[self.difficulty]
	if self.humanoid_first:
            player_one = Humanoid(self.token_one)
	    player_two = ai_object(self.token_two)
	else:
            player_one = ai_object(self.token_two)
	    player_two = Humanoid(self.token_one)
	return Game(player_one,player_two)

    @staticmethod
    def prompts():
	return HumanPromptInterface.prompts()
