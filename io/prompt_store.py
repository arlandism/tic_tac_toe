from collections import OrderedDict

class PromptStore(object):

    def __init__(self):
        self.player_choices = ("Human","Humanoid","ImpossibleAI","EasyAI")
        self.game_prompts = OrderedDict()
        self.game_prompts[self.player_string()] = self.player_choices
        self.game_prompts[self.first_token()] = ("x","o")
        self.game_prompts[self.second_player()] = self.player_choices 
        self.game_prompts[self.board()] = (3,4)

    def player_string(self):
        return "The first player is a...\n" + "\n".join(self.player_choices) 
    def first_token(self):
        return "What's the first player's token (x or o)? "

    def second_player(self):
        return "What kind of player will be moving second? "

    def board(self):
        return "Board size please (3 or 4)"

