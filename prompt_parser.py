from prompt_store import PromptStore
from token_info import TokenInfo as ti

class PromptParser(object):

    def __init__(self,user_data):
        self.user_data = user_data

    def first_token(self):
        return self.user_data.get(PromptStore().first_token(),-1)

    def second_token(self):
        return ti.other_token(self.first_token()) 

    def first_player(self):
        return self.user_data.get(PromptStore().player_string())

    def second_player(self):
        return self.user_data.get(PromptStore().second_player())

    def board_size(self):
        return self.user_data.get(PromptStore().board())
