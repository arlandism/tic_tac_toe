from collections import OrderedDict

class PromptStore(object):

    game_prompts = OrderedDict()
    player_string = ("\nHuman\n" + "Humanoid\n" + "ImpossibleAI\n" + "EasyAi\n")
    game_prompts["What's the first player's token (x,o)? "] = ("x","o")
    game_prompts["The first player is a..." + player_string] = ("Human","Humanoid","ImpossibleAI","EasyAi")
    game_prompts["And the second... same options "] = ("Human","Humanoid","ImpossibleAI","EasyAi")
    game_prompts["Board size please... "] = (3,4)
