from game import Game
from humanoid import Humanoid
from ai import ImpossibleAI
from human_prompt_interface import HumanPromptInterface
from minimax import Minimax
from human_setup import HumanSetup

class HumanoidVsAiScenario(object):

    def __init__(self,user_data):
        self.setup_obj = HumanSetup(user_data)
        self.ai_hash = {"easy":Minimax(self.setup_obj.opp_token(),1),"impossible":Minimax(self.setup_obj.opp_token(),20)}

    def setup(self):
        minimax_level = self.ai_hash[self.setup_obj.difficulty()]
        ai_token = self.setup_obj.opp_token()
        if self.setup_obj.user_first():
            player_one = Humanoid(self.setup_obj.human_token())
            player_two = ImpossibleAI(ai_token,minimax=minimax_level)
        else:
            player_one = ImpossibleAI(ai_token,minimax=minimax_level)
            player_two = Humanoid(self.setup_obj.human_token())
        return Game(player_one,player_two)

    @staticmethod
    def prompts():
        return HumanPromptInterface.prompts()
