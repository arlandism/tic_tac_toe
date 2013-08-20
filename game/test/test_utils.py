from players.player import HumanPlayer

class MockFactory(object):

   @staticmethod
   def player(player_type,token,display_object=None):
       return player_type

class MockPlayer(HumanPlayer):

    def __init__(self,token,fake_input):
        super(MockPlayer,self).__init__(token,fake_input)
