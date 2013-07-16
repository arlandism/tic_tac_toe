from collections import OrderedDict

class PromptStore(object):

    player_choices = ("Human","Humanoid","ImpossibleAI","EasyAI")
    game_prompts = OrderedDict()
    game_prompts["What's the first player's token (x,o)? "] = ("x","o")
    game_prompts["The first player is a...\n" + "\n".join(player_choices)] = player_choices 
    game_prompts["And the second... same options "] = player_choices 
    game_prompts["Board size please... "] = (3,4)
