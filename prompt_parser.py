
class PromptParser(object):

    def __init__(self,user_data):
        self.user_data = user_data

    def first_token(self):
        return self.user_data.get("What's the first player's token (x,o)? ",-1)

    def second_token(self):
        first_token = self.first_token()
        return {"x":"o","o":"x"}.get(first_token,-1)

    def first_player(self):
        player_string = ("\nHuman\n" + "Humanoid\n" + "ImpossibleAI\n" + "EasyAi\n")
        return self.user_data.get("The first player is a..." + player_string)

    def second_player(self):
        return self.user_data.get("And the second... same options ")

    def board_size(self):
        return self.user_data.get("Board size please... ")
