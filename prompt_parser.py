from prompt_store import PromptStore

class PromptParser(object):

    def __init__(self,user_data):
        self.user_data = user_data

    def first_token(self):
        return self.user_data.get(PromptStore().first_token(),-1)

    def second_token(self):
        first_token = self.first_token()
        return {"x":"o","o":"x"}.get(first_token,-1)

    def first_player(self):
        return self.user_data.get(PromptStore().player_string())

    def second_player(self):
        return self.user_data.get(PromptStore().second_player())

    def board_size(self):
        return self.user_data.get(PromptStore().board())
