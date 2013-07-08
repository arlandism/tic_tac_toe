from player import HumanPlayer
from human_prompt_interface import HumanPromptInterface
from easy_ai import EasyAI
from ai import ImpossibleAI
from game import Game

class HumanVsAiScenario(object):
    
    def __init__(self,user_data):
	 self.human_first = {1:True,2:False}[user_data.get("Would you like to move first or second (1,2): ")] 
	 self.human_token = user_data.get("Would you like to play as x or o: ")
	 self.ai_token = {"x":"o","o":"x"}[self.human_token] 
	 self.difficulty = user_data.get("Would you like to play against an easy or impossible ai: ")
	 self.ai_hash = {"easy":EasyAI,"impossible":ImpossibleAI}

    def setup(self):
	ai_object = self.ai_hash[self.difficulty]
	if self.human_first:
	    player_one = HumanPlayer(self.human_token)
	    player_two = ai_object(self.ai_token)
	else:
	    player_one = ai_object(self.ai_token)
	    player_two = HumanPlayer(self.human_token)
	return Game(player_one,player_two)

    @staticmethod
    def prompts():
	return HumanPromptInterface.prompts()
