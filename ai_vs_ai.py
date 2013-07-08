from ai import ImpossibleAI
from game import Game
from no_prompt_interface import NoPromptInterface
from easy_vs_impossible_ai import EasyVsImpossibleAiScenario

class AiVsAiScenario(object):

    def __init__(self,user_data):
	self.difficulty = user_data.get("What difficulty would you like the first ai to be (easy,impossible): ")

    def setup(self):
	if self.difficulty == "easy":
            return EasyVsImpossibleAiScenario().setup()
        return NoPromptInterface().setup(ImpossibleAI)

    @staticmethod
    def prompts():
	difficulty_prompt = {"What difficulty would you like the first ai to be (easy,impossible): ":
			     ("easy","impossible")}
	# Passes prompts to OrderedDict creator
	return NoPromptInterface.prompts(difficulty_prompt)
