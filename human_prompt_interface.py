from collections import OrderedDict

class HumanPromptInterface(object):

    @staticmethod
    def prompts(*more_prompts):
	current_prompts = OrderedDict()
	current_prompts["Would you like to move first or second (1,2): "] = (1,2)
	current_prompts["Would you like to play as x or o: "] = ("x","o")
	current_prompts["Would you like to play against an easy or impossible ai: "] = ("easy","impossible") 
	for prompt_hash in more_prompts:
	    current_prompts.update(prompt_hash)
	return current_prompts

