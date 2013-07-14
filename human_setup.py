
class HumanSetup(object):

    def __init__(self,data):
        self.user_data = data
        self.humanish_token = self.user_data.get("Would you like to play as x or o: ",-1)
        self.opponent_token = {"x":"o","o":"x"}.get(self.humanish_token,-1)
        self.user_move = self.user_data.get("Would you like to move first or second (1,2): ",-1)
        self.ai_level = self.user_data.get("Would you like to play against an easy or impossible ai: ",-1)

    def human_token(self):
        return self.humanish_token

    def opp_token(self):
        return self.opponent_token

    def user_first(self):
        return {1:True,2:False}[self.user_move]

    def difficulty(self):
        return self.ai_level

        
