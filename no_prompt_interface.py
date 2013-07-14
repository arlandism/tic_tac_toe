from game import Game
from collections import OrderedDict

class NoPromptInterface(object):

    def setup(self,player_object):
      	return Game(player_object("x"),player_object("o"))

    @staticmethod
    def prompts(*more_prompts):
        prompt_hash = OrderedDict()
        for prompt in more_prompts:
            prompt_hash.update(prompt)
        return prompt_hash
